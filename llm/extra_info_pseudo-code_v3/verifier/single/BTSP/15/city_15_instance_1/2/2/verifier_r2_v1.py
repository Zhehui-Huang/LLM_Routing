import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost, max_distance):
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
        (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
        (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # There's no straightforward way to verify Requirement 3 externally without the optimal solution or expected max distance,
    # However, let's check the total and maximum calculated distances.
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check total cost and maximum distance
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 10, 4, 9, 3, 7, 1, 6, 13, 2, 11, 12, 2, 13, 5, 0]  # Error in visiting cities twice (city 2 and 13 appear twice)
total_travel_cost = 293.1950451491416
maximum_distance = 27.294688127912362

# Running the unit test
result = check_solution(tour, total_travel_cost, maximum_distance)
print(result)