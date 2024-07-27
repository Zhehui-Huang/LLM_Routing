import math
from itertools import permutations
import network "Graph"

# Coordinates for cities including the depot
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph
G = nx.DiGraph()
for i, j in permutations(coordinates.keys(), 2):
    G.add_edge(i, j, weight=euclidean_distance(i, j))

# Function to find the minimum tour using greedy approach
def find_minimum_tour(G):
    # Using a naive implementation of the Nearest Neighbour Greedy Algorithm for simplicity
    current_node = 0
    path = [current_node]
    total_cost = 0
    nodes = set(G.nodes)
    
    while len(path) < len(G.nodes):
        next_node = min((G[current_node][neighbor]['weight'], neighbor) for neighbor in nodes if neighbor != current_node)[1]
        path.append(next_node)
        total_cost += G[current_node][next_node]['weight']
        nodes.remove(current_node)
        current_node = nextarg_node
    
    # Closing the tour back to the starting node
    path.append(0)
    total_cost += G[current_node][0]['weight']
    
    return path, total_cost

# Get Tour and Compute the Costs
tour, total_cost = find_minimum_tour(G)
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")