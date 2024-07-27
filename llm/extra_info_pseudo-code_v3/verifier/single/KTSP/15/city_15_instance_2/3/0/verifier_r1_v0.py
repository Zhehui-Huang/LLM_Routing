import numpy as np
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def test_solution(tour, total_travel_cost):
    # Coordinates for each city index
    cities = {
        0: (54, 87),
        2: (69, 84),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        10: (51, 28),
        12: (56, 58)
    }
    
    # Requirement 1: Start and end at depot city, index 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 8 cities including the depot city
    if len(tour) != 8:
        return "FAIL"
    
    # Check if each city index in the tour exists in known city coordinates
    for city in tour:
        if city not in cities.keys() and city != 0:
            return "FAIL"
    
    # Requirement 3: Calculate the travel cost and compare with given total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city_a][0], cities[city_a][1], cities[city_b][0], cities[city_b][1])
    
    if not np.isclose(calculated_cost, total_travel_cost, atol=0.01):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 6, 5, 10, 4, 12, 2, 0]
total_travel_cost = 149.73

# Perform the test
result = test_solution(tour, total_travel_cost)
print(result)