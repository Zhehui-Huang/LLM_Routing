import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Verify tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(i not in visited for i in range(len(cities))):
        return "FAIL"

    # Verify travel cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided cities and their coordinates
cities = [
    (84, 67),  # Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Solution provided
tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
total_cost = 294.17

# Verification
result = verify_solution(tour, total_width, cities)
print(result)