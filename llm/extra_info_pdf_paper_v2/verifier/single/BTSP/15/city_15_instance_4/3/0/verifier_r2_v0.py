import math

# Provided data
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
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_tour(tour):
    total_cost = 0
    max_distance = 0

    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        total_cost += distance
        max_distance = max(max_distance, distance)

    # Checking requirements
    correct_start_end = tour[0] == tour[len(tour) - 1] == 0  # Requirement 1 and 5
    all_visited_once = len(set(tour[1:-1])) == 14  # Requirement 2
    correct_total_cost = math.isclose(total_cost, 337.84, rel_tol=1e-5)  # Requirement 6
    correct_max_distance = math.isclose(max_distance, 60.67, rel_tol=1e-5)  # Requirement 7

    # Output determination based on all conditions being True
    if correct_start_end and all_visited_once and correct_total_hr_cost and correct_metric and correct_structure:
        print("CORRECT")
    else:
        print("FAIL")

tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
verify_tour(tour)