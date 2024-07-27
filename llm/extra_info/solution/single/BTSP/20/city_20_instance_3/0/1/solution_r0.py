import math
import itertools

# Define the cities and their positions
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# TSP Function to find the optimal route
def solve_tsp():
    n = len(cities)
    all_city_indices = range(n)
    min_route = None
    min_max_distance = float('inf')
    min_total_cost = float('inf')
    
    # Explore all permutations of city visits starting at city 0 to minimize the longest distance
    for perm in itertools.permutations(all_city_indices[1:]):
        route = [0] + list(perm) + [0]
        max_distance = 0
        total_cost = 0
        
        # Calculate costs for this permutation
        for i in range(n):
            dist = euclidean_distance(route[i], route[i+1])
            total_cost += dist
            if dist > max_distance:
                max_const = dist
        
        # Check if this permutation is better
        if max_distance < min_max_distance:
            min_route = route
            min_max_distance = max_distance
            min_total_cost = total_cost
    
    return min_route, min_total_cost, min_max_distance

# Function to perform the operation and print output
def perform_operation():
    optimal_tour, total_travel_cost, max_distance_consec_cities = solve_tsp()
    print(f"Tour: {optimal_tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance_consec_cities}")

# Run the task
perform_operation()