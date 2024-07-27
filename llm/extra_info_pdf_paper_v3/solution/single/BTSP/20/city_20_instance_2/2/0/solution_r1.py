import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the tour with minimized maximum distance between consecutive cities
def find_optimal_tour():
    num_cities = len(cities)
    best_tour = None
    best_max_distance = float('inf')
    
    # Generate all possible tours starting and ending at the depot (city 0)
    all_tours = permutations(range(1, num_cities))  # Generate permutations for cities 1 to 19
    
    for tour in all_tours:
        # Append the depot city to the start and end of the tour
        current_tour = [0] + list(tour) + [0]
        
        # Calculate the maximum distance between consecutive cities in the current tour
        max_distance_in_tour = max(
            euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1)
        )
        
        # If the found tour has a smaller maximum distance, update the best tour found
        if max_distance_in_tour < best_max_distance:
            best_max_distance = max_distance_in_tour
            best_tour = current_tour
    
    # Calculate total travel cost for the best tour
    total_travel_cost = sum(
        euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1)
    )
    
    return best_tour, total_travel_cost, best_max_distance

# Get the results of the calculations
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))