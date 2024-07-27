import math

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Test data - robot tours and city coordinates
cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 1, 4, 0]
robot_1_tour = [0, 18, 13, 15, 16, 17, 12, 14, 11, 10, 0]

def test_tour(tour):
    """ Helper function to determine whether a given tour meets the start and end constraints. """
    return tour[0] == tour[-1] == 0

def test_unique_visitation(robot_0_tour, robot_1_tour):
    """ Check if all cities (except the depot) are visited exactly once. """
    all_cities_combo = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    return all_cities_combo == set(range(1, 19))

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of a given tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    return total_cost

# Conduct the test for Robot 0 and Robot 1 tours
test_robot_0 = test_tour(robot_0_tour)
test_robot_1 = test_tour(robot_1_tour)
test_unique = test_unique_visitation(robot_0_tour, robot_1_tour)
correct_costs_robot_0 = math.isclose(calculate_tour_cost(robot_0_tour), 121.84817612829175, rel_tol=1e-5)
correct_costs_robot_1 = math.isclose(calculate_tour_cost(robot_1_tour), 149.76726379384303, rel_tol=1e-5)

# Final verification result
if test_robot_0 and test_robot_1 and test_unique and correct_costs_robot_0 and correct_costs_robot_1:
    print("CORRECT")
else:
    print("FAIL")