import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_solution(tour, cost, coordinates):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits exactly 6 cities
    if len(set(town for town in tour if tour.count(town) == 1)) + 1 != 6:
        return "FAIL"

    # Check if the computed travel cost matches the expected cost
    computed_cost = total_travel_cost(tour, coordinates)
    if not math.isclose(computed_cost, cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Cities coordinates
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Given tour and its total travel cost
tour = [0, 8, 5, 2, 1, 9, 0]
cost = 183.85

# Verify the solution
result = verify_solution(tour, cost, coordinates)
print(result)