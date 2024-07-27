import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: The tour does not start and end at the depot city 0."
    
    if len(set(tour)) != 8:
        return "FAIL: The total number of distinct cities visited is not exactly 8."
    
    if len(tour) != 8:  # The list should contain exactly 8 indices including starting and ending at the depot
        return f"FAIL: The tour length is not correct. Expected 8 (including repeating the depot), got {len(tour)}."
    
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean distance(cities[tour[i-1]], cities[tour[i]])
    
    if not math.isclose(total_travel_cost, calculated_cost, abs_tol=1e-2):
        return f"FAIL: The reported total travel cost {total_travel_cost} does not match the calculated cost {calculated_cost}."
    
    return "CORRECT"

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    7: (97, 70),
    9: (66, 62)
}

# Provided solution data
tour = [0, 1, 3, 4, 5, 7, 9, 0]
total_travel_cost = 254.30537537633583

# Run verification and print the result
verification_result = verify_solution(tour, total_travel_cost, cities)
print(verification_result)