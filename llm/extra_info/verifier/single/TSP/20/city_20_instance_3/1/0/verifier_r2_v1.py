import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95),
        (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit all cities exactly once and return to the depot
    visited_cities = tour[1:-1]
    unique_visited = set(visited_cities)
    if len(visited_cities) != len(unique_visited) or set(range(1, 20)) != unique_visited:
        return "FAIL"

    # Requirement 3: Calculate and check the travel cost
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        computed_total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066

# Verifying the provided solution
result = verify_solution(tour, total_travel_cost)
print(result)