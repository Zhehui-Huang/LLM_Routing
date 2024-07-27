import math
import networkx as nx
from itertools import permutations

# Coordinates for each city indexed from 0 to 9
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

# Calculate Euclidean distance between two cities
def euclidean_distance(cityA, cityB):
    x1, y1 = cityA
    x2, y2 = cityB
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours that return to the starting city
def generate_tours(nodes):
    for perm in permutations(nodes):
        # Start and end at the depot city, 0
        yield (0,) + perm + (0,)

# Evaluate a tour by computing its total cost and max edge cost
def evaluate_tour(tour):
    total_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        edge_cost = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += edge_msg
        if edge_cost > max_edge_cost:
            max_edge_cost = edge_cost
    return total_cost, max_edge_cost

# Main function to find the optimal tour
def find_optimal_tour():
    best_tour = None
    lowest_max_edge_cost = float('inf')
    lowest_total_cost = float('inf')

    for tour in generate_tours(range(1, 10)):  # Generate tours excluding the depot which is fixed at start and end
        total_cost, max_edge_cost = evaluate_tour(tour)
        # We aim to minimize the maximum distance between consecutive cities
        if max_edge_cost < lowest_max_edge_cost or (max_edge_cost == lowest_max_edge_cost and total_cost < lowest_total_cost):
            best_tour = tour
            lowest_max_edge_cost = max_edge_cost
            lowest_total_cost = total_cost

    return best_tour, lowest_total_cost, lowest_max_edge_cost

# Execute the function
optimal_tour, total_travel_cost, max_distance = find_optimal_tour()

# Outputting results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")