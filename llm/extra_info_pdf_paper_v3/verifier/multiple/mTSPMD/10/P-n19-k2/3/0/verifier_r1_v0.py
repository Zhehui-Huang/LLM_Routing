import math

# City coordinates
cities = [
    (30, 40), # 0
    (37, 52), # 1
    (49, 43), # 2
    (52, 64), # 3
    (31, 62), # 4
    (52, 33), # 5
    (42, 41), # 6
    (52, 41), # 7
    (57, 58), # 8
    (62, 42), # 9
    (42, 57), # 10
    (27, 68), # 11
    (43, 67), # 12
    (58, 27), # 13
    (37, 69), # 14
    (61, 33), # 15
    (62, 63), # 16
    (63, 69), # 17
    (45, 35)  # 18
]

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tours(tours):
    """ Check if the solution meets the conditions """
    visited = set()
    total_cost_computed = 0
    depot_cycles = set()

    for robot_id, tour in enumerate(tours):
        # Check if the start and end are same.
        if tour[0] != tour[-1]:
            return "FAIL: Tour must start and end at the same city"

        # Check if cities visited exactly once plus start and end city
        tour_non_repeats = set(tour[1:-1])
        if len(tour_non_repeats | set(tour[:1])) + visited & tour_non_repeats:
            return "FAIL: Each city must be visited exactly once by any robot"
        visited.update(tour_non_repeats)
        total_cost = 0
        
        # Calculate the cost of this tour
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        
        # Check against reported total cost
        expected_cost = round(total_cost, 2)
        provided_cost = round(tour_costs[robot_id], 2)
        if expected_cost != provided_cost:
            return f"FAIL: Cost discrepancy. Expected: {expected_cost}, Provided: {provided_cost}"
        
        total_cost_computed += total_cost
        depot_cycles.add(tour[0])

    # Verify all cities are visited
    if len(visited) != 17:
        return "FAIL: Not all cities are visited"

    # Check depot cycles
    if len(depot_cycles) != 2:
        return "FAIL: Incorrect depot visits"

    # Validate overall cost
    if round(total_cost_computed, 2) != round(overall_cost, 2):
        return "FAIL: Overall cost discrepancy"

    return "CORRECT"

# Outputs from solution
robot_0_tour = [0, 6, 10, 14, 3, 2, 7, 15, 5, 0]
robot_1_tour = [1, 4, 11, 12, 17, 16, 8, 9, 13, 18, 1]
tour_costs = [102.71, 115.71]
overall_cost = 218.42

# Run verification
print(verify_tours([robot_0_tour, robot_1_tuyır]))