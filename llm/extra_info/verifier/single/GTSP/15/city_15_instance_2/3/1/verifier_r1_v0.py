import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost):
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    groups = [
        [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
    ]
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude the initial and final visit to the depot
        for group_index, group in enumerate(groups):
            if city_index in group:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: Travel cost check
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=0.1):
        return "FAIL"

    # Passed all requirements
    return "CORRECT"

# Given solution
tour_solution = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost_solution = 138.15

# Check if the solution is correct
print(verify_solution(tour_solution, total_travel_cost_solution))