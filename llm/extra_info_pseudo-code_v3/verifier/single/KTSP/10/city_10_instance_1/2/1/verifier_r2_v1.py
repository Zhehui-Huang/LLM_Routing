import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_positions):
    # [Requirement 1] Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Exactly 5 cities including the depot
    if len(tour) != 6:
        return "FAIL"

    # [Requirement 5] Tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check for unique cities within the tour (excluding the initial city since it repeats at the end)
    unique_cities = set(tour[:-1]) # remove the last depot entry for uniqueness check
    if len(unique_cities) != 5:
        return "FAIL"

    # [Requirement 3 & 6] Check the total calculated travel cost
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])

    if not math.isclose(total_cost, calculated_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Additional specific checks can be added here if more solution constraints are needed.
    return "CORRECT"

# Define city positions (based on document input)
city_positions = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Provided tour and cost
tour = [0, 2, 9, 7, 1, 0]
total_cost = 200

# Verify solution
result = verify_solution(tour, total_cost, city_positions)
print(result)