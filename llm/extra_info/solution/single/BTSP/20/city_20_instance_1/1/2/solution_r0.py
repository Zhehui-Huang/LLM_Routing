import math
import itertools

# Define cities' coordinates
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate pairwise city distances
dist_matrix = {}
for c1 in cities:
    for c2 in cities:
        dist_matrix[(c1, c2)] = distance(c1, c2)

# Heuristic: Nearest Neighbor modified to minimize the maximum leg length of the tour
def find_minimax_tour(start, cities):
    unvisited = set(cities)
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[(current_city, city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Complete the tour
    tour.append(start)
    return tour

def evaluate_tour(tour):
    total_cost = sum(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_dist = max(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost, max_dist

# Generating an initial tour
initial_tour = find_minimax_tour(0, cities)
total_cost, max_dist = evaluate_tour(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")