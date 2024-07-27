import numpy as np

# Define the coordinates of the cities
cities = np.array([
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
])

# Given solution details
tour = [0, 1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18, 0]
total_travel_cost = 1034.66
max_distance = 82.29

def calculate_euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour(tour, cities):
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except for the depot (city 0)
    if sorted(tour) != sorted([0] + list(range(1, len(cities)))):
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check against given costs with a small tolerance due to floating point precision
    if not (np.isclose(calculated_total_cost, total_travel_cost, atol=1e-2) and 
            np.isclose(calculated_max_distance, max_distance, atol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Check the given solution
result = check_tour(tour, cities)
print(result)