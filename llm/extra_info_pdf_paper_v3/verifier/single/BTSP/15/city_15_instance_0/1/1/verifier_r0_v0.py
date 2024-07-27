import numpy as np

def calculate_euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost, max_distance):
    # City Coordinates
    cities = {
        0: (9, 93),
        8: (19, 76),
        10: (19, 65)
    }
    
    # [Requirement 1] Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    visited_cities = set(tour[1:-1])  # Exclude the depot city at the start/end
    if len(visited_cities) != len(tour) - 2:  # Subtract 2 for the repeating depot city
        return "FAIL"
    
    # [Requirement 3] Check if max distance between any two consecutive cities is correctly computed
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        distance = calculate_euclidean_distance(cities[city_index_1], cities[city_index_2])
        calculated_max_distance = max(calculated_max_distance, distance)
        
    if not np.isclose(calculated_max_distance, max_distance, atol=0.001):
        return "FAIL"

    # Calculate total travel cost and compare
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        calculated_total_dist = calculate_euclidean_distance(cities[city_index_1], cities[city_index_2])
        calculated_total_cost += calculated_total_dist

    if not np.isclose(calculated_total_cost, total_cost, atol=0.001):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 8, 10, 0]
total_travel_cost = 60.45522041795303
maximum_distance_between_cities = 29.732137494637012

# Test the provided solution
result = test_solution(tour, total_travel_LOOt, maximum_distance_between_cities)
print(result)