import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, cost):
    # Define the cities as per problem statement
    cities = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }

    # [Requirement 1] Check if start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Verify each city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"

    # [Requirement 3] Check the total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(calculated_cost - cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Input the tour and total cost from problem solution
tour_input = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_cost_input = 477.0516251264448

# Output RESULT
print(verify_solution(tour_input, total costs_input))