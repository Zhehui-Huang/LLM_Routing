import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Constant for the provided tour and cost
    cities = [
        (79, 15),  # Depot city 0
        (79, 55),  # City 1
        (4, 80),   # City 2 (excluded in solution)
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8 (excluded in solution)
        (66, 62)   # City 9
    ]

    # [Requirement 1] Check if the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if the tour includes exactly 8 different cities
    expected_city_count = 8
    # Exclude start/end city which is the depot indexed by 0
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != expected_city_count - 1:  # excluding depot city from the count
        return "FAIL"

    # [Requirement 5] Check if the total travel cost is calculated and matches the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # Uses len(unique_cities) + 1 due to depot city and requirements 2 ensures exactly 8 cities are visited including depot
    if len(unique_cities) + 1 != expected_city_count:
        return "FAIL"

    return "CORRECT"

# Example solution provided
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_cost = 235.38

# Run verification
print(verify_solution(tour, total_cost))