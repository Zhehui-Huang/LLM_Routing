import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_tsp_solution():
    # Given city coordinates
    cities_coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Provided tour and its cost
    tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 3, 4, 6, 10, 15, 0]
    claimed_total_cost = 390.80

    # Check number of cities
    if len(cities_coordinates) != 20:
        return "FAIL"

    # Check the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    unique_cities_visited = set(tour[1:-1])
    if len(unique_cities_visited) != 19 or any(city not in unique_cities_visited for city in range(1, 20)):
        return "FAIL"

    # Calculate the actual travel cost in the claimed tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])

    if not math.isclose(actual_cost, claimed_total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Running the test function
result = test_tsp_solution()
print(result)