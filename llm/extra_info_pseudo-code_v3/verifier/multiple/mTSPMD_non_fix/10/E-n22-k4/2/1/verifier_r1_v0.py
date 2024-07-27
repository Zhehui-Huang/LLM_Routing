import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, costs, cities, num_robots):
    visited_cities = set()
    total_calculated_cost = 0.0

    # City coordinates as given in the description
    city_coords = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    # Check for each robot
    for i in range(num_robots):
        tour = tours[i]
        expected_cost = costs[i]
        tour_cost = 0.0

        # Check if the length matches and starts at depot city 0
        if tour[0] != 0:
            print("Robot starts at wrong depot.")
            return "FAIL"

        # Calculate travel cost for the tour
        for j in range(1, len(tour)):
            tour_cost += euclidean_distance(city_coords[tour[j-1]], city_coords[tour[j]])
            visited_cities.add(tour[j])

        # Add cost from last city to the end city
        if i in [0, 1, 2, 3]:  # We assume endpoint not necessary to be depot, just for validation has to exist.
            # Check if it stops at any possible city as endpoint
            if tour[-1] not in city_coords:
                print("Robot ends at invalid city.")
                return "FAIL"

        # Check if the calculated cost matches the expected
        if not math.isclose(tour_cost, expected_cost, abs_tol=1e-2):
            print(f"Cost mismatch: calculated {tour_cost}, expected {expected_cost}")
            return "FAIL"
            
        total_calculated_cost += tour_cost

    # Check if all cities were visited exactly once
    all_cities = set(cities)
    if visited_cities != all_cities:
        print("Not all cities visited exactly once or some cities visited more than once.")
        return "FAIL"

    # Check if the overall cost is correct
    overall_cost = sum(costs)
    if not math.isclose(total_calculated_cost, overall_at_cost, abs_tol=1e-2):
        print(f"Overall cost mismatch: calculated {total_calculated_cost}, provided overall cost {overall_cost}")
        return "FAIL"

    return "CORRECT"

# Test data
cities = range(22)
num_robots = 4
tours = [
    [0, 14, 17, 20, 10, 5, 4],
    [0, 16, 19, 21, 9, 2],
    [0, 12, 15, 18, 7, 1],
    [0, 13, 11, 8, 6, 3]
]
costs = [137.51, 127.28, 111.48, 75.14]
overall_at_cost = 451.40

# Running the test
result = verify_solution(tours, costs, cities, num_robots)
print(result)