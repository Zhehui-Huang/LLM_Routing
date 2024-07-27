import math
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a complete graph with cities as nodes and distances as edge weights
def create_complete_graph():
    G = nx.Graph()
    for (city1, city2) in combinations(cities, 2): # combinations for undirected graph
        G.add_edge(city1, city2, weight=euclidean_distance(city1, city2))
    return G

# Function to calculate the total and maximum distance in the tour
def calculate_distances(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    return total_distance, max_distance

# Main function setting up the graph and finding the optimal path
def find_optimal_tour():
    G = create_complete_graph()
    # Using the greedy approach to approximate the solution due to complexity constraints
    t_path = nx.approximation.greedy_tsp(G, source=0)
    t_path.append(t_path[0])  # Complete the tour by returning to the depot

    total_cost, max_leg_distance = calculate_distances(t_path)

    # Return relevant values as a dictionary for clear output
    return {
        'Tour': t_path,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_leg_distance
    }

# Execute the function and capture results
results = find_optional_tour()

# Print the output
print("Tour:", results['Tour'])
print("Total travel cost:", results['Total travel cost'])
print("Maximum distance between consecutive cities:", results['Maximum distance between consecutive cities'])