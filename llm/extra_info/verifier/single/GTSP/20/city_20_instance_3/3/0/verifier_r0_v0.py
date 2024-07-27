import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, calculated_cost):
    city_positions = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    city_groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]
    
    # Requirement 1: Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude starting 0 and ending 0
        for idx, group in enumerate(city_groups):
            if city in group:
                visited_groups[idx] += 1
                if visited_groups[idx] > 1:
                    return "FAIL"

    if not all(visited == 1 for visited in visited_groups):
        return "FAIL"
    
    # Requirement 3 and 5: Calculate and compare the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 4: Implicitly checked by input format of tour
    return "CORRECT"

# Provided solution test data
tour_solution = [0, 4, 7, 12, 15, 3, 18, 0]
total_travel_cost_solution = 227.40171050114

# Test the solution
test_result = test_solution(tour_solution, total_travel_compile_cost_solution)
print(test_result)