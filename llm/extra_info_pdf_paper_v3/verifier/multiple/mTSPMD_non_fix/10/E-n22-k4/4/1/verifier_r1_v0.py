import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Configuring the initial city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Tour information for verification
robot_tours = [
    [0, 16, 17, 18, 12, 8],
    [1, 5, 4, 13, 15, 20],
    [2, 6, 10, 11, 19],
    [3, 7, 9, 14, 21]
]

# Calculated costs for verification
robot_costs = [
    92.54170976723009,
    154.38588660309497,
    96.02845633471095,
    99.248598341517
]

# Verify that all cities are visited once
def test_all_cities_visited_once():
    visited = set()
    for tour in robot_tours:
        visited.update(tour)
    return len(visited) == len(city_coordinates)

# Verify the travel cost for each robot tour
def test_robot_tour_costs():
    calculated_costs = []
    for tour in robot_tours:
        cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = city_coordinates[tour[i]]
            x2, y2 = city_coordinates[tour[i + 1]]
            cost += calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_costs.append(cost)
    return all(math.isclose(calculated_costs[i], robot_costs[i], rel_tol=1e-9) for i in range(len(robot_costs)))

# Test the overall total cost
def test_overall_cost():
    return math.isclose(sum(robot_costs), 442.204651046553, rel_tol=1e-9)

def run_tests():
    if not test_all_cities_visited_once():
        return "FAIL: Not all cities are visited exactly once."
    if not test_robot_tour_costs():
        return "FAIL: Incorrect travel costs for one or more robot tours."
    if not test_overall_cost():
        return "FAIL: Incorrect overall travel cost."
    return "CORRECT"

# Run the verification tests
test_result = run_tests()
print(test_result)