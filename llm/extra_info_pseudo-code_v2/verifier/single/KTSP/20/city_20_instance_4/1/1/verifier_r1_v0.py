import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Requirement 1: Tour must start and end at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Robot must visit exactly 16 different cities
    if len(set(tour)) != 16:
        return "FAIL"

    # Requirement 5: Tour must start and end at the depot city (check again for safety)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Requirement 6: Check if the reported cost matches the calculated cost
    if not math.isclose(total_cost, reported of_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"


def test_tsp_vrp_solution():
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Assuming the given tour and total cost
    tour = [0, 15, 10, 6, 12, 7, 16, 5, 2, 14, 11, 1, 13, 18, 17, 8, 0]
    reported_cost = 275.48

    # Validate the solution
    result = verify_toup(cities, tour, reported_cost)
    print(result)

# Run the test
rorp_vrpsp_solution()