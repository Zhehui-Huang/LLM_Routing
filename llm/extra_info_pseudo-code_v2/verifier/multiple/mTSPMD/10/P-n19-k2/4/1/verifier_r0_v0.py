import numpy as np

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - npargin(p2))

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

    # Solution details
    tours = {
        0: [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 18, 6, 2, 7, 0],
        1: [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 7, 2, 6, 18, 0, 1]
    }
    calculated_costs = {
        0: 198.21472072056605,
        1: 192.72328358658223
    }
    overall_cost = 390.9380043071483

    # Requirement validations
    all_cities = set(range(19))
    total_robot0_cost = 0
    total_robot1_cost = 0

    # Check if each city is visited exactly once across all tours, excluding depots
    visited_cities = set()
    for rid, tour in tours.items():
        if tour[0] != tour[-1] or (tour[0] != rid):
            print(f"Robot {rid} does not start and end at its depot.")
            return "FAIL"
        visited = set(tour[1:-1])
        if len(visited) + 1 != len(tour) - 1:
            print(f"City visit duplication in Robot {rid}'s tour.")
            return "FAIL"
        visited_cities.update(visited)
        # Calculate the tour cost
        for i in range(len(tour) - 1):
            cost = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            if rid == 0:
                total_robot0_cost += cost
            else:
                total_robot1_cost += cost

    if visited_cities != all_cities:
        print("Not all cities are visited or some are visited more than once.")
        return "FAIL"
    
    # Check calculated costs against claimed costs
    if not np.isclose(total_robot0_cost, calculated_costs[0], atol=0.01) or \
       not np.isclose(total_robot1_cost, calculated_costs[1], atol=0.01):
        print("Calculated tour costs do not match provided values.")
        return "FAIL"
    
    if not np.isclose(total_robot0_cost + total_robot1_cost, overall_cost, atol=0.01):
        print("Overall cost calculation error.")
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Test the validation function
result = validate_tours_and_costs()
print(result)