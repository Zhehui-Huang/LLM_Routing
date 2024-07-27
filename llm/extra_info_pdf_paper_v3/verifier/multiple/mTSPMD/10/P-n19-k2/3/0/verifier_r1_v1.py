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

def verify_tours(tours, tour_costs, overall_cost):
    """ Check if the solution meets the conditions """
    visited = set()
    total_cost_computed = 0

    for robot_id, tour in enumerate(tours):
        # Check if the start and end are the same city.
        if tour[0] != tour[-1]:
            return "FAIL: Tour must start and end at the same city"

        # Track and check city visits
        cities_in_tour = set(tour[1:-1])
        if visited.intersection(cities_in_tour):
            return "FAIL: Cities visited more than once across all tours"
        visited.update(cities_in_tour)
        
        # Compute and verify the travel cost of the tour
        total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        if round(total_cost, 2) != round(tour_costs[robot_id], 2):
            return f"FAIL: Cost mismatch in robot {robot_id}'s tour"

        total_cost_computed += total_cost

    # Verify all cities were visited exactly once and tours start and end at their respective depots
    if len(visited) != len(cities) - 2 or any(robi[0] != robi[-1] for robi in tours):
        return "FAIL: Cities visitation error"

    # Validate summed cost accuracy
    if round(total_cost_computed, 2) != round(overall_cost, 2):
        return "FAIL: Overall cost discrepancy"

    return "CORRECT"

# Test inputs (adjusted for typo in the second robot tour reference)
robot_0_tour = [0, 6, 10, 14, 3, 2, 7, 15, 5, 0]
robot_1_tour = [1, 4, 11, 12, 17, 16, 8, 9, 13, 18, 1]
tour_costs = [102.71, 115.71]
overall_cost = 218.42

# Test the solution
result = verify_tours([robot_0_tour, robot_1_tour], tour_costs, overall_cost)
print(result)