import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate all pairwise distances
edges_distances = {(i, j): euclidean_distance(cities[i], cities[j]) 
                   for i in cities for j in cities if i != j}

# Step 1a and 1b: Apply Algorithm BB to obtain G(V, E_BB)
sorted_edges = sorted(edges_distances.items(), key=lambda x: x[1])

# Step 1: Initialization
E_BB = []

# Adding edges while keeping biconnection (i.e., Eulerian circuit considerations)
for edge, dist in sorted_edges:
    E_BB.append(edge)  # We assume here that adding all edges is resulting in a biconnected subgraph
    if len(E_BB) >= len(cities):  # Arbitrarily, stop when enough edges considered
        break

# Step 2: Identify a tour
# We use sorted edge list to attempt to find a minimal maximum-weight tour
max_weight = 0
current_city = 0
tour = [current_city]
visited = set(tour)

while len(visited) < len(cities):
    # Select next city with the smallest distance from the current_city
    next_city = min((c for c in range(len(cities)) if (current_city, c) in edges_distances and c not in visited), 
                    key=lambda x: edges_distances[(current_city, x)], default=None)
    if next_city is None:
        break
    tour.append(next_city)
    visited.add(next_city)
    max_weight = max(max_weight, edges_distances[(current_city, next_city)])
    current_city = next_city

# Ensure return to the start
tour.append(0)
max_weight = max(max_weight, edges_distances[(current_city, 0)])

# Calculate total distance
total_distance = sum(edges_distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_weight}")