import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Check Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Tour must include exactly 7 cities
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check Requirement 3: Calculate the actual travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i+1]
        calculated_cost += calculate_euclidean_distance(*cities[city_a], *cities[city_b])

    # Using a tolerance for floating point arithmetic comparison
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 8, 3, 7, 1, 4, 0]
total_travel_cost = 128.73130793605634

# Verify the provided solution
solution_status = verify_solution(tour, total_travel_cost)
print(solution_status)