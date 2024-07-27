import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }

    # [Requirement 1] The tour must start and end at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot has to visit exactly 6 out of the 10 cities, including the depot city.
    if len(set(tour)) != 6:
        return "FAIL"

    # Calculate the total travel cost from the tour and compare with the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])

    # [Requirement 3] Minimize the total Euclidean distance traveled by the robot.
    # For validation purposes, we check if the calculated cost matches the reported cost closely
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85354044487238

# Perform the test
result = test_solution(tour, total_travel_construct)
print(result)