import math

# Define city coordinates, including the depot
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Provided tours for each robot
solutions = {
    0: [0, 12, 14, 15, 16, 18, 0],
    1: [0, 3, 4, 6, 8, 10, 11, 0],
    2: [0, 13, 17, 19, 20, 21, 0],
    3: [0, 1, 2, 5, 7, 9, 0]
}

# Expected travel costs for each tour
expected_costs = [121.20933003054614, 124.23927957725854, 138.2546749628742, 111.83855721201843]
expected_total_cost = 495.5418417826973

def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    total_cost = 0
    visited_cities = set()

    for robot_id, tour in solutions.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check each city in the tour except the starting and ending depot
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculate and validate the travel cost of each robot's tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_euclidean_distance(*city_coords[tour[i]], *city_coords[tour[i + 1]])
            tour_cost += distance
        
        # Check if the calculated distance matches the expected distance
        if not math.isclose(tour_cost, expected_costs[robot_id], abs_tol=1e-5):
            return "FAIL"
        
        total_cost += tour_cost

    if len(visited_cities) != 21:
        return "FAIL"

    if not math.isclose(total_cost, expected_total_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Output the test result
print(test_solution())