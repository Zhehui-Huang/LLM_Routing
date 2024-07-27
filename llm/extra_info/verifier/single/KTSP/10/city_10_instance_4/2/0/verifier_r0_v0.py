import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: The tour does not start and end at the depot city 0."
    
    if len(set(tour)) != 8:
        return "FAIL: The total number of distinct cities visited is not 8."
    
    if len(tour) != 7 + 1:  # 7 cities + 1 return to depot (the list should contain exactly 8 indices including repetitions)
        return "FAIL: The tour does not have 8 stops including returning to the depot city."
    
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    if not math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-5):
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

# Given solution data
tour = [0, 1, 3, 4, 5, 7, 9, 0]
total_travel_cost = 254.30537537633583

# Run the verification
verification_result = verify_solution(tour, total_travel_actions, cities)
print(verification_result)