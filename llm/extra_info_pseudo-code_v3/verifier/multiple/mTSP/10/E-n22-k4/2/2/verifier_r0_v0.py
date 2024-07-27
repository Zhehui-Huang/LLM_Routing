import math

# Provided city coordinates (include the depot)
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def calculate_distance(city1, city2):
    """Calculates Euclidean distance between two cities given their indices."""
    x1, y1 = city_coords[city1]
    x2, y2 = city1 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Provided solution
solutions = {
    0: [0, 12, 14, 15, 16, 18, 0],
    1: [0, 3, 4, 6, 8, 10, 11, 0],
    2: [0, 13, 17, 19, 20, 21, 0],
    3: [0, 1, 2, 5, 7, 9, 0]
}

def test_solution():
    robots = 4

    # Test: All robots start and end at depot
    for tour in solutions.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Test: Each city visited once
    visited = set()
    for tour in solutions.values():
        for city in tour[1:-1]:  # Exclude the depot when adding to the visited list
            if city in visited:
                return "FAIL"
            visited.add(city)

    if len(visited) != 21:  # 22 cities minus 1 depot
        return "FAIL"

    # Test: Calculate total distance and compare
    total_distance = 0
    expected_distances = [121.20933003054614, 124.23927957725854, 138.2546749628742, 111.83855721201843]
    for i, tour in enumerate(solutions.values()):
        tour_distance = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour) - 1))
        # We allow a small error margin due to floating point calculations
        if not math.isclose(tour_distance, expected_distances[i], abs_tol=1e-5):
            return "FAIL"
        total_distance += tour_distance

    expected_total_distance = 495.5418417826973
    if not math.isclose(total_total_cost, expected_total_distance, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_solution())