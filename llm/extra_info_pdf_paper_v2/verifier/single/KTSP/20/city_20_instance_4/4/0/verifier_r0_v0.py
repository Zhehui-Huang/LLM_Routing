import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, reported_cost):
    # Coordinates of the cities
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Requirements checking:
    # Requirement 1 and Requirement 6
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    if len(set(tour)) != 16 or len(tour) != 17:
        return "FAIL"

    # Requirement 3 and Requirement 5
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        total_cost_calculated += calculate_euclidean_and_infrastructure_cost(cities[city_1], cities[city_2])

    # Requirement 4: We cannot assure the shortest possible tour but reported cost must match calculated.
    if round(total_cost_calculated, 6) != round(reported_cost, 6):
        return "FAIL"

    return "CORRECT"

# Replace these values with the actual tour and cost results you need to verify
tour = [0, 12, 10, 1, 2, 3, 4, 6, 11, 16, 5, 9, 18, 15, 7, 14, 0]
total_cost = 775.843658223079

def calculate_euclidean_and_infrastructure_cost(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return calculate_euclidean_distance(x1, y1, x2, y2)

# Perform the test
result = verify_solution(tour, total_cost)
print(result)