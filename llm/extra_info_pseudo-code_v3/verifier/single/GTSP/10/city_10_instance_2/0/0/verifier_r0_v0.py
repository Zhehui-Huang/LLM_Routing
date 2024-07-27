import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost_calculated):
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    groups = {
        0: [3, 6],
        1: [5, 8],
        2: [4, 9],
        3: [1, 7],
        4: [2]
    }
    
    # Check if starts and ends at depot 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for group_id, cities_in_group in groups.items():
            if city in cities_in_group:
                if groupID in visited_groups:
                    return "FAIL"
                visited_groups.append(groupID)
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check if total travel cost is correctly calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost_calculated, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution tour and cost
tour_provided = [0, 3, 5, 2, 1, 9, 0]
total_cost_provided = 273.31

# Verify the solution
result = verify_solution(tour_provided, total_cost_provided)
print(result)