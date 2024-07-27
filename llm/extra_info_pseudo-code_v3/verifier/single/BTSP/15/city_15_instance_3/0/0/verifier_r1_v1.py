import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour_solution(tour, cities, expected_cost, expected_max_dist):
    """Verify tour solution against provided requirements."""
    # [Requirement 4] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Check if the robot visits each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(city not in unique_cities for city in cities.keys()):
        return "FAIL"
    
    # [Requirement 5] Calculate the total cost of the provided tour
    total_cost = 0
    max_distance = 0
    last_city = tour[0]
    for current_city in tour[1:]:
        dist = calculate_distance(cities[last_city], cities[current_city])
        total_cost += dist
        # [Requirement 3] Tracking maximum distance between any two consecutive cities in the tour
        if dist > max_distance:
            max_distance = dist
        last_test_city = current_city
    
    # Check total travel cost and max distance against expected values
    if not math.isclose(total_cost, expected_cost, abs_tol=0.01):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_dist, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates indexed by city number (assuming 0-indexed, first city is depot)
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

tour = [0, 1, 3, 12, 4, 5, 6, 8, 11, 2, 7, 10, 9, 13, 14, 0]
total_travel_cost = 396.97
maximum_distance = 48.37

# Verify the solution
result = verify_tour_solution(tour, cities, total_travel_cost, maximum_distance)
print(result)