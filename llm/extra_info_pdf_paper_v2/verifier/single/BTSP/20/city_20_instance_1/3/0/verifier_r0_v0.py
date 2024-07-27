import numpy as np

# Coordinates of cities (index 0 is the depot)
cities_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), 
    (68, 98), (45, 84), (4, 56), (54, 82), 
    (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), 
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Solution from the previous message
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 6, 2, 9, 13, 8, 1, 15, 18, 17, 19, 12, 0]
total_travel_cost = 503.93280249020313
max_distance = 96.1041102138717

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def verify_solution(tour, cities_coords, total_travel_cost, max_distance):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check if all cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    # Calculate the actual distances and validate against provided max distance and total cost
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities_coords[tour[i]], cities_coords[tour[i+1]])
        actual_total_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist
    # Check computed max distance and total travel cost
    if not np.isclose(actual_total_cost, total_travel_export, atol=0.01):
        return "FAIL"
    if not np.isclose(actual_max_distance, max_distance, atol=0.01):
        return "FAIL"
    return "CORRECT"

# Calling the verification function and print output
print(verify_solution(tour, cities_coords, total_travel_cost, max_distance))