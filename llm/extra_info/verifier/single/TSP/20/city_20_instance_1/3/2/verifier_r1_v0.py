import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour_and_cost(cities, tour, reported_cost):
    # Verify the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Verify each city is visited exactly once, except the depot which should be visited twice (start and end)
    if sorted(tour) != sorted([0] + list(range(1, 20)) + [0]):
        return False

    # Verify the calculated cost matches the reported cost
    total_computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_computed_cost += calculate_euclidean_distance(cities[city_a][0], cities[city_a][1], cities[city_b][0], cities[city_b][1])

    if not math.isclose(total_computed_cost, reported_cost, rel_tol=1e-9):
        return False

    return True

# Coordinates of cities indexed from 0 to 19
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9),
}

# Provided solution
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_cost = 477.0516251264448

# Check if the solution is correct
if verify_tour_and_cost(cities, tour, total_cost):
    print("CORRECT")
else:
    print("FAIL")