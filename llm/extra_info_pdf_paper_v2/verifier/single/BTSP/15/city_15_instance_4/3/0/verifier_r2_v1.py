import math

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour):
    if not tour:
        print("FAIL: Tour is empty")
        return

    total_cost = 0
    max_distance = 0
    visited_cities = set()

    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = euclidean_distance(city1, city2)
        total_cost += distance
        max_distance = max(max_distance, distance)
        visited_cities.add(city1)

    # Check all requirements:
    correct_start_end = (tour[0] == 0 and tour[-1] == 0)  # Requirement 1 and 5
    all_visited_once = (len(visited_cities) == 14 and len(tour) == 16)  # Requirement 2
    correct_total_cost = (math.isclose(total_cost, 337.84, rel_tol=1e-3))  # Requirement 6
    correct_max_distance = (math.isclose(max_distance, 60.67, rel_tol=1e-3))  # Requirement 7

    if correct_start_end and all_visited_once and correct_total_cost and correct_max_distance:
        print("CORRECT")
    else:
        print("FAIL")

# Tour provided for testing
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
verify_tour(tour)