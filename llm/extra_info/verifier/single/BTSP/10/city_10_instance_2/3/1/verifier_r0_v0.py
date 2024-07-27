import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, city_coordinates):
    # Check if tour starts and ends at the depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once (Requirement 2)
    visited_cities = tour[1:-1]
    if len(visited_cities) != len(set(visited_cities)) or set(visited_cities) != set(range(1, 10)):
        return "FAIL"
        
    # Calculate the total distance and the maximum distance (Requirement 3)
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
        total_distance += dist
        max_distance = max(max_distance, dist)

    expected_total_distance = 409.3392018720813
    expected_max_distance = 73.348483283569
    if abs(total_distance - expected_total_distance) > 1e-6 or abs(max_distance - expected_max_distance) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# City coordinates provided in the task
city_coords = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Provided tour solution
tour_solution = [0, 4, 9, 1, 2, 5, 7, 6, 3, 8, 0]

# Execute the test
test_output = test_solution(tour_solution, city_coords)
print(test_output)