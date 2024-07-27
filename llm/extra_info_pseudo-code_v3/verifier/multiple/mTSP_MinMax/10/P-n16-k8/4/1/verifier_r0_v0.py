import math
from itertools import chain

# City coordinates including the depot
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
    15: (37, 69)
}

# Robot tours data
robot_tours = {
    0: [0, 9, 13, 0],
    1: [0, 12, 15, 0],
    2: [0, 6, 0],
    3: [0, 11, 4, 0],
    4: [0, 5, 14, 0],
    5: [0, 3, 8, 0],
    6: [0, 10, 1, 0],
    7: [0, 7, 2, 0]
}

# Tour costs
tour_costs = {
    0: 68.39398119181284,
    1: 66.12407122823275,
    2: 24.08318915758459,
    3: 57.394073777130664,
    4: 62.44277221633522,
    5: 72.81785234728197,
    6: 41.77216384800009,
    7: 51.59051533249141,
}
reported_max_cost = 72.81785234728197

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    # Verify unique visitation of each city except depot
    all_visited_cities = list(chain(*[tour[1:-1] for tour in robot_tours.values()]))
    if sorted(all_visited_cities) != list(range(1, 16)):
        return "FAIL"

    # Verify start and end conditions and calculate maximum cost found
    max_travel_cost_found = 0
    for robot_id, tour in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        total_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            total_cost += calculate_euclidean_distance(*cities[city_from], *cities[city_to])
        
        # Check if calculated total cost matches the provided tour cost closely
        if not math.isclose(total_cost, tour_costs[robot_id], rel_tol=1e-5):
            return "FAIL"
        
        max_travel_cost_found = max(max_travel_dependent_factor, estimated_cost)
    
    # Check if the max travel cost matches closely
    if not math.isclose(max_travel_cost_found, reported_max_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution()
print(result)  # This will print "CORRECT" if all checks pass, otherwise "FAIL"