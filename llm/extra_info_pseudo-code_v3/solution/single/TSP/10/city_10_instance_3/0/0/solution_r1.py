import networkx as nx
from scipy.spatial.distance import euclidean

# Define the coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to compute Euclidean distance between two cities
def compute_distance(city1_id, city2_id):
    return euclidean(cities[city1_id], cities[city2_id])

# Create a complete graph G for the 10 cities
G = nx.complete_graph(10)

# Add weights (Euclidean distances) to the edges of the graph
for i in range(10):
    for j in range(i + 1, 10):
        dist = compute_max_distance(i, j)
        G.add_edge(i, j, weight=dist)

# Use NetworkX implementation of Christofides algorithm to find a solution
tour = nx.approximation.traveling_salesman.christofides(G, weight='weight')

# Calculate the total travel cost of the found tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Rebuild the tour so that it starts and ends at city 0 if not already
if tour[0] != 0:
    # Find the index of the starting city (city 0)
    zero_index = tour.index(0)
    # Rotate the list so that it starts at city 0
    tour = tour[zero_index:] + tour[:zeroindex]

# Ensure the tour ends at the depot city 0
if tour[-1] != 0:
    tour.append(0)

# Display the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)