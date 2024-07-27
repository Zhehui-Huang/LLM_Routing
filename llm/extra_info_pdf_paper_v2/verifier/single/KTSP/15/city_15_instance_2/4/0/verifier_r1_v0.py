import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, expected_cost):
    # Cities as (x, y) coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    
    # Requirement 1: Check if tour is starting and ending at the depot city and includes exactly 8 cities
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != 9:  # including city 0 twice
        return "FAIL"

    # Requirement 2: Validate the cost calculation
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_travel_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    # Passed all the requirements
    return "CORRECT"

# Provided solution information
tour = [0, 13, 3, 12, 2, 11, 8, 1, 0]
total_travel_cost = 156.81

# Validate the solution
result = verify_solution(tour, total_travel_cost)
print(result)