import math

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities, total_cost, max_consecutive_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1: Start and end at depot city (city 0)
    
    if len(set(tour)) != len(cities) or sorted(set(tour)) != sorted(list(range(len(cities)))):
        return "FAIL"  # Requirement 2: Each city visited exactly once

    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Allow for minor floating point discrepancies
    if abs(calculated_total_cost - total_cost) > 0.01 or abs(calculated_max_distance - max_consecutive_distance) > 0.01:
        return "FAIL"  # Requirement 3: Check distances and total cost

    return "CORRECT"

# City coordinates (index corresponds to city number)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided solution details
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.37
maximum_distance = 68.15

# Check if the provided solution is correct
result = verify_tour(tour, cities, total_travel_cost, maximum_distance)
print(result)