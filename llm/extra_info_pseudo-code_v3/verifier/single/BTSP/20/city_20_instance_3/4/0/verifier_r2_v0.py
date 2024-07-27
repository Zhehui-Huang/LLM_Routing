import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the cities (positions)
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Solution provided
tour_solution = [0, 1, 7, 14, 8, 12, 18, 4, 10, 11, 9, 16, 17, 15, 3, 5, 2, 13, 6, 19, 0]  # corrected tour (removed the extra 0)
total_cost_solution = 482.40
max_distance_solution = 41.00

# Functions to test the constraints and requirements
def test_start_end_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_visit_once(tour):
    return len(set(tour)) == len(tour)  # Includes only one depot, as it starts and ends there

def test_travel_distance(tour, expected_total_cost):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return math.isclose(total_cost, expected_total_cost, abs_tol=0.01) and math.isclose(max_distance, max_distance_solution, abs_tol=0.01)

def test_complete_tour(tour):
    visited = set(tour)
    return len(visited) == len(cities) and all(city in visited for city in cities)

# Running the tests
if (test_start_end_depot(tour_solution) and
    test_visit_once(tour_solution) and
    test_travel_distance(tour_solution, total_cost_solution) and
    test_complete_tour(tour_solution)):
    print("CORRECT")
else:
    print("FAIL")