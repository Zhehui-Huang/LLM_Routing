import math

def calculate_euclidean_distance(a, b):
    """Calculate Euclidean distance between two 2D points a and b."""
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def verify_requirements():
    # City coordinates as given
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    # Provided tours and costs
    tours_and_costs = {
        0: {
            'tour': [0, 16, 10, 4, 12, 18, 8, 2, 14, 20, 6, 0],
            'reported_cost': 143.10076079569438
        },
        1: {
            'tour': [1, 7, 5, 17, 9, 13, 19, 3, 15, 11, 1],
            'reported_cost': 130.26686823139715
        }
    }
    overall_reported_cost = 273.36762902709154

    all_visited_cities = set()

    # [Requirement 1] Check for correct depot starts and ends
    if tours_and_costs[0]['tour'][0] != 0 or tours_and_costs[0]['tour'][-1] != 0:
        return "FAIL"
    if tours_and_costs[1]['tour'][0] != 1 or tours_and_costs[1]['tour'][-1] != 1:
        return "FAIL"
    
    # [Requirement 2] Check if all cities are visited exactly once
    for robot_id, data in tours_and_costs.items():
        tour = data['tour']
        if len(tour) != len(set(tour)) - 1:  # exclude repeated depot visit
            return "FAIL"
        all_visited_cities.update(tour[1:-1])  # exclude depots

    if all_visited_cities != set(cities.keys()) - {0, 1}:
        return "FAIL"

    # [Requirement 4] Calculating the actual travel costs and [Requirement 5] verifying
    total_calculated_cost = 0
    for robot_id, data in tours_and_costs.items():
        tour = data['tour']
        cost = sum(
            calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            for i in range(len(tour) - 1)
        )
        if not math.isclose(cost, data['reported_cost'], rel_tol=1e-5):
            return "FAIL"
        total_calculated_cost += cost

    # [Requirement 3] Check if the combined total cost is minimal and correctly reported
    if not math.isclose(total_calculated_cost, overall_reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "COR "

if __name__ == "__main__":
    result = verify_requirements()
    print(result)