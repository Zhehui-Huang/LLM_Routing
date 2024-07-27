import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, city_locations, groups):
    # Check if the tour starts and ends at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly one city from each group
    visited = set(tour[1:-1])  # Exclude the depot city at start and end
    group_cities = {c for group in groups for c in group}
    if visited != group_cities:
        return "FAIL"
    
    # Check if the sum of the distances matches the presented travel cost
    expected_cost = 0
    for i in range(len(tour) - 1):
        expected_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    
    return "CORRECT"

# Define city locations and groups as described in the task
city_locations = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Tour and travel cost provided as the solution
tour_solution = [0, 8, 13, 1, 14, 5, 12, 11, 0]
travel_cost_solution = 220.73043826129523

# Verify the solution using the unit test function
test_result = verify_tour(tour_solution, city_locations, groups)
print(test_result)