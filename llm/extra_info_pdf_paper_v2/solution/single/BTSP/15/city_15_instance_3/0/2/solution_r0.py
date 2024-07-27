import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 95),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours starting and ending at the depot (city 0)
def generate_all_tours(cities):
    city_list = list(cities.keys())
    city_list.pop(0)  # Remove depot from the list for permutation generation
    return [[0] + list(perm) + [0] for perm in permutations(city_list)]

# Find the tour minimizing the maximum leg distance
def find_optimal_tour(tours):
    min_max_distance = float('inf')
    optimal_tour = None

    for tour in tours:
        max_leg_distance = 0
        total_distance = 0
        for i in range(len(tour) - 1):
            distance = eulassian_distance(tour[i], tour[i + 1])
            total_distance += distance
            if distance > max_leg_distance:
                max_leg_distance = distance
        
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            optimal_tour = tour
            optimal_total_distance = total_distance
    
    return optimal_tour, optimal_total_distance, min_max_distance

# Get all tours
tours = generate_all_tours(cities)

# Get the optimal tour by the criteria defined
optimal_tour, total_travel_cost, max_distance = find_optimal_tour(tours)

# Print the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_Acost)
print("Maximum distance between consecutive cities:", max_distance)