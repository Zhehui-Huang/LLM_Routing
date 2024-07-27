import math
from itertools import permutations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to evaluate the tour: Total cost and maximum edge cost
def evaluate_tour(tour):
    total_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
    return total_cost, max_edge_cost

# Brute force approach to find the best tour that minimizes the maximum distance between any two cities
def find_best_tour():
    n = len(cities)
    all_tours = permutations(range(1, n))  # generate all permutations of city indices except the depot
    best_tour = None
    best_max_edge = float('inf')
    best_total_cost = float('inf')

    for tour in all_tours:
        # Append the depot city (0) at the start and end of the tour
        complete_tour = [0] + list(tour) + [0]
        total_cost, max_edge_cost = evaluate_tour(complete_tour)
        
        # Check if the current tour has a lower max edge cost
        if max_edge_cost < best_max_edge or (max_edge_cost == best_max_edge and total_cost < best_total_cost):
            best_max_edge = max_edge_cost
            best_total_adjusted = total_cost
            best_tour = complete_tour

    return best_tour, best_total_adjusted, best_max_edge

# Calculate and print the best tour, its total cost and maximum distance between consecutive cities
best_tour, total_cost, max_edge_cost = find_best_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")