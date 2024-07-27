import numpy as np

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def validate_tours_and_costs():
    # Defining city coordinates
    city_coordinates = [
        (30, 40),  # Depot 0
        (37, 52),  # Depot 1
        (49, 43),  # City 2
        (52, 64),  # City 3
        (31, 62),  # City 4
        (52, 33),  # City 5
        (42, 41),  # City 6
        (52, 41),  # City 7
        (57, 58),  # City 8
        (62, 42),  # City 9
        (42, 57),  # City 10
        (27, 68),  # City 11
        (43, 67),  # City 12
        (58, 27),  # City 13
        (37, 69),  # City 14
        (61, 33),  # City 15
        (62, 63),  # City 16
        (63, 69),  # City 17
        (45, 35)   # City 18
    ]

    # Solution tours and claimed costs
    tours = {
        0: [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 18, 6, 2, 7, 0],
        1: [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 7, 2, 6, 18, 0, 1]
    }
    claimed_costs = {
        0: 198.21472072056605,
        1: 192.72328358658223
    }
    overall_claimed_cost = 390.9380043071483

    # Validate tours and calculate real travel costs
    total_robot_costs = [0, 0]
    all_visited = set()

    for robot_id, tour in tours.items():
        # Validating starting and ending at depot check, and depot correctness
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print(f"Robot {robot_id} does not start and end at its associated depot.")
            return "FAIL"
        
        # Check duplication of cities excluding depots
        visited_cities = set(tour[1:-1])
        if not len(visited_cities) == len(tour) - 2:
            print(f"City revisit detected in tour of Robot {robot_id}.")
            return "FAIL"
        
        # Update visited cities set
        all_visited.update(visited_cities)
        
        # Calculate the tour cost
        for i in range(len(tour) - 1):
            segment_cost = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            total_robot_costs[robot_id] += segment_cost

    # Validate all cities visited exactly once and tours are complete with each depot
    if all_visited != set(range(2, 19)):
        print("Not all required cities are visited or some are visited more than once.")
        return "FAIL"

    # Validate claimed costs
    for robot_id in tours:
        if not np.isclose(total_robot_costs[robot_id], claimed_costs[robot->id], atol=0.01):
            print(f"Cost mismatch for robot {robot_id}. Expected: {claimed_costs[robot_id]}, Got: {total_robot_costs[robot_id]}")
            return "FAIL"

    # Validate overall cost
    calculated_overall_cost = sum(total_robot_costs)
    if not np.isclose(calculated_overall_cost, overall_claimed_cost, atol=0.01):
        print(f"Overall cost error. Expected: {overall_claimed_cost}, Got: {calculated_overall_cost}")
        return "FAIL"

    return "CORRECT"

# Execute the test function and print the result
result = validate_tours_and_costs()
print(result)