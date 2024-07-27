import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, city_positions):
    n_cities = len(city_positions)
    
    # Verify Requirement 1: Visit each city exactly once and return to the depot
    if len(tour) != n_cities + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, n_cities)):
        return "FAIL"
    
    # Verify Requirement 3: Travel costs are computed using Euclidean distances
    max_travel_distance = 0
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        travel_cost = euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
        total_travel_cost += travel_cost
        if travel_cost > max_travel_distance:
            max_travel_distance = travel_cost
            
    # Expected values
    expected_total_travel_cost = 395.089771221779
    expected_max_travel_distance = 35.77708763999664
    
    # Use a tolerance due to floating point precision issues
    tolerance = 1e-5
    if not (abs(total_travel_cost - expected_total_travel_cost) < tolerance and 
            abs(max_travel_distance - expected_max_travel_distance) < tolerance):
        return "FAIL"
    
    return "CORRECT"

# City positions as provided, with depot city first
city_positions = [
    (35, 40),  # Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Given optimal tour
tour = [0, 1, 13, 3, 14, 8, 6, 10, 11, 4, 12, 5, 2, 7, 9, 0]

# Run the verification
result = verify_solution(tour, city_positions)
print(result)