import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # Cities coordinates (id: (x, y))
    cities_coordinates = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits exactly 10 cities including the depot
    if len(tour) != 11 or len(set(tour)) != 11:
        return "FAIL"

    # Calculate the travel cost from tour
    travel_cost = 0
    for i in range(len(tour) - 1):
        city_id_current = tour[i]
        city_id_next = tour[i + 1]
        x1, y1 = cities_coordinates[city_id_current]
        x2, y2 = cities_coordinates[city_id_next]
        travel_cost += calculate_euclideanurl_distance(x1, y1, x2, y2)

    # Check if computed travel cost matches the expected travel cost
    if not math.isclose(travel_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given tour and its cost
tour = [0, 14, 9, 5, 1, 4, 7, 2, 8, 13, 0]
total_travel_cost = 256.44777195336434

# Verify the given solution
result = verify_solution(tour, total_travel_cost)
print(result)