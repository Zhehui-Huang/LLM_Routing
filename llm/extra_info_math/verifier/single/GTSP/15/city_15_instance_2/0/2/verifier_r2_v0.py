import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_robot_tour_solution(tour, cost):
    # Cities coordinates
    cities = {
        0: (54, 87),
        1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
        6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
        11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # City groups
    groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    
    # Requirement 1: Starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits exactly one city from each city group
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # skipping the depot city in the checking
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
                break
    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 3: Minimize total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Tolerance for float comparison
    if not math.isclose(calculated_cost, cost, rel_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour_provided = [0, 6, 0]
cost_provided = 10.770329614269007

# Test the solution
result = test_robot_tour_solution(tour_provided, cost_provided)
print(result)