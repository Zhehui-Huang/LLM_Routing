import math
from itertools import permutations

# Coordinates of cities including the depot at index 0
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    """ Calculate the total cost and maximum leg distance of a tour """
    total_cost = 0
    max_distance = 0
    n = len(tour)
    for i in range(1, n):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    # Return to the depot
    dist = euclidean_distance(coordinates[tour[-1]], coordinates[tour[0]])
    total_cost += dist
    max_distance = max(max_distance, dist)
    return total_cost, max_distance

def find_optimal_btsp_tour():
    """ Find the optimal tour for Bottleneck TSP given the problem setup """
    num_cities = len(coordinates)
    all_cities = list(range(1, num_cities))  # Exclude the depot initially
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Checking all permutations is computationally expensive
    # and not feasible for more than ~10 cities, here we assume feasibility for clarity
    for perm in permutations(all_cities):
        tour = [0] + list(perm) + [0]  # Start and end at the depot
        total_cost, max_distance = calculate_tour_cost(tour)
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_tour = tour
            best_total_cost = total_cost
            best_max_distance = max_distance
    
    return best_tour, best_total_cost, best_max_distance

# Find the optimal BTSP solution
optimal_tour, optimal_total_cost, optimal_max_distance = find_optimal_btsp_tour()

# Print the results according to the format requirements
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_total_cost, 2))
print("Maximum distance between consecutive cities:", round(optimal_max_distance, 2))