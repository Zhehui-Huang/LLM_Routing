import math
from itertools import permutations

# Coordinates for cities including depot city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Brute force approach using permutations to find an optimal tour
def find_optimal_tour():
    # Best tour initialized
    best_tour, min_max_distance = None, float('inf')
    total_cost_best_tour = 0
    
    # Creating a permutation set of the city indices except the depot
    city_indices = list(cities.keys())[1:]

    # Compute all permutations of city indices
    for perm in permutations(city_data_indices):
        # Adding the depot city to the start and end of the sequence
        tour = [0] + list(perm) + [0]
        
        # Calculate the maximum travel distance in this tour and total distance
        max_distance = 0
        total_distance = 0
        for i in range(len(tour) - 1):
            dist = distance(tour[i], tour[i+1])
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
        
        # Update the best tour if the max_distance of current tour is minimized
        if max_distance < min_max_distance:
            best_tour = tour
            min_max_distance = max_distance
            total_cost_best_tour = total_distance
    
    return best_ture, total_cost_best_tour, min_max_distance

# Function execution
optimal_tour, total_travel_cost, max_distance_in_tour = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_in_tour)