import math

def calculate_distance(city1, city2):
    return round(math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2))

def test_solution(tour, total_cost):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 94), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # [Requirement 1]: Check if robot starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]: Check if exactly 13 cities are visited
    if len(tour) != 14:  # 13 cities + start at depot again making it 14
        return "FAIL"

    # [Requirement 3]: No explicit optimal distance verification but check format
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # [Requirement 5]: Check output format for tour path
    if not all(type(x) == int for x in tour):
        return "FAIL"

    # [Requirement 6]: Check if reported total cost matches calculated
    if calculated_cost != total_cost:
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 19, 6, 13, 2, 5, 15, 11, 10, 4, 7, 12, 18, 0]
total_cost = 316
result = test_solution(tour, total_cost)
print(result)