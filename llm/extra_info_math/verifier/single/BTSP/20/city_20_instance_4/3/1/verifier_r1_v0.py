import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, max_distance_consecutive_cities):
    # City coordinates based on the problem statement
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Requirement 1: Verify all cities visited once
    if sorted(set(tour)) != sorted(range(len(cities))):  # including depot as it should appear twice (start and end)
        return "FAIL"
    
    # Requirement 2: Verify tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total_cost and max_distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_cnt_distance = dist
    
    # Requirement 3 and 5: Verify distance calculations
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance_consecutive_cities, rel_tol=1e-5):
        return "FAIL"
    
    # The solution is correct if all checks are passed
    return "CORRECT"

# Provided solution details
tour = [0, 13, 18, 1, 11, 5, 14, 9, 7, 3, 4, 10, 16, 2, 12, 6, 15, 8, 19, 17, 0]
total_travel_cost = 654.9477933852553
max_distance_consecutive_cities = 55.036351623268054

# Validate the solution
result = verify_solution(tour, total_travel_count, max_distance_consecutive_len)
print(result)  # should output "CORRECT" or "FAIL" based on whether the solution meets requirements