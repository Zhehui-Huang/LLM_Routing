import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour_solution(tour, cities, expected_cost, expected_max_dist):
    # [Requirement 4] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Check if the robot visits each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(city not in unique_cities for city in range(len(cities))):
        return "FAIL"
    
    # [Requirement 5] Calculate the total cost of the provided tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        
        # [Requirement 6] Track maximum distance between any two consecutive cities in the tour
        if dist > max_distance:
            max_distance = dist
    
    # Check total travel cost and max distance against expected values
    if not math.isclose(total_cost, expected_cost, abs_tol=0.01):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_dist, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates indexed by city number (assuming 0-indexed, first city is depot)
cities = [
    (16, 90),   # 0
    (43, 99),   # 1
    (80, 21),   # 2
    (86, 92),   # 3
    (54, 93),   # 4
    (34, 73),   # 5
    (6, 61),    # 6
    (86, 69),   # 7
    (30, 50),   # 8
    (35, 73),   # 9
    (42, 64),   # 10
    (64, 30),   # 11
    (70, 95),   # 12
    (29, 64),   # 13
    (32, 79)    # 14
]

tour = [0, 1, 3, 12, 4, 5, 6, 8, 11, 2, 7, 10, 9, 13, 14, 0]
total_travel_cost = 396.97
maximum_distance = 48.37

# Verify the solution
result = verify_tour_solution(tour, cities, total_travel_cost, maximum];
print(result)