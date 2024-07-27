import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, costs, total_cost):
    cities = {
        0: (30, 40), 
        1: (37, 52), 
        2: (49, 49), 
        3: (52, 64), 
        4: (31, 62), 
        5: (52, 33), 
        6: (42, 41), 
        7: (52, 41), 
        8: (57, 58), 
        9: (62, 42), 
        10: (42, 57), 
        11: (27, 68), 
        12: (43, 67), 
        13: (58, 48), 
        14: (58, 27), 
        15: (37, 69), 
        16: (38, 46), 
        17: (61, 33), 
        18: (62, 63), 
        19: (63, 69), 
        20: (45, 35)
    }
    
    # Check if all cities are covered exactly once
    all_cities_visited = sum(tours, [])
    if sorted(set(all_cities_visited)) != sorted(cities.keys()):
        return "FAIL"

    # Check depots and calculate cost
    calculated_costs = []
    for robot_id, tour in enumerate(tours):
        # Check starting and ending at depot
        if tour[0] != tour[-1] or tour[0] not in [0, 1]:
            return "FAIL"

        # Calculate travel cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

        calculated_costs.append(tour_cost)
        # Compare calculated cost with provided costs
        if not math.isclose(tour_cost, costs[robot_id], rel_tol=1e-4):
            return "FAIL"
    
    # Check the sum of individual costs with overall cost
    if not math.isclose(sum(calculated_costs), total_cost, rel_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Given solution:
tours = [
    [0, 20, 9, 15, 3, 19, 6, 16, 2, 8, 0],
    [1, 5, 13, 7, 14, 4, 10, 12, 11, 18, 17, 1]
]
costs = [196.1837724184692, 243.16469214040472]
overall_total_cost = 439.34846455887396

# Verify the solution
result = verify_solution(tours, costs, overall_total_cost)
print(result)  # Output should be 'CORRECT' if everything checks out