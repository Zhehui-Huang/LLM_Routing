import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost):
    cities = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
        (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
        (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
    ]

    # [Requirement 1] Start and end at the depot city, 0
    check1 = tour[0] == 0 and tour[-1] == 0

    # [Requirement 2] Visit exactly 10 cities, including the depot
    unique_cities = set(tour)
    check2 = len(unique_cities) == 10 and 0 in unique_cities

    # [Requirement 3] Not validatable merely by output
    # Skipping as it requires comparing against all possible tours

    # [Requirement 4] Correct calculation of travel cost
    calculated_distance = 0
    for i in range(len(tour) - 1):
        calculated_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    check4 = math.isclose(calculated_distance, total_cost, rel_tol=1e-2)

    # [Requirement 5] The tour output is a list of city indices - visible from input type
    check5 = isinstance(tour, list) and all(isinstance(x, int) for x in tour)

    # [Requirement 6] The travel cost is output correctly - visible from input type
    check6 = isinstance(total_cost, (int, float))

    # Final result
    if check1 and check2 and check4 and check5 and check6:
        return "CORRECT"
    else:
        return "FAIL"

# Example tour and cost from previous solution provided.
tour = [0, 14, 9, 13, 8, 10, 7, 12, 4, 1, 0]
total_cost = 201.34

result = test_solution(tour, total_cost)
print(result)