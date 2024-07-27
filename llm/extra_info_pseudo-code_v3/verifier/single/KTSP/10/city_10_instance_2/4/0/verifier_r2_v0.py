import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def check_start_and_end_city(tour, depot):
    """Check whether the robot starts and ends at the depot city."""
    assert tour[0] == depot and tour[-1] == depot, "Tour must start and end at the depot."

def check_number_of_cities_visited(tour):
    """Check if exactly 6 different cities are visited."""
    assert len(set(tour)) == 6, "Tour should visit exactly 6 different cities."

def check_travel_cost(tour, coordinates, expected_cost):
    """Calculate travel cost and compare with expected cost."""
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    assert round(total_cost, 2) == round(expected_cost, 2), "Calculated travel cost does not match the expected cost."

def test_solution():
    city_coordinates = {0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
                        5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)}
    tour = [0, 5, 9, 2, 1, 8, 0]
    expected_cost = 203.4060363709706

    try:
        check_start_and_end_city(tour, 0)
        check_number_of_cities_visited(tour)
        check_travel_cost(tour, city_coordinates, expected_cost)
        print("CORRECT")
    except AssertionError as e:
        print("FAIL:", str(e))

# Perform the test
test_solution()