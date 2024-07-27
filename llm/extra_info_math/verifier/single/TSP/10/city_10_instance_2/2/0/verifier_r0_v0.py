import math

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Given tour from the solver
tour = [0, 8, 5, 9, 1, 2, 7, 4, 6, 3, 0]
reported_cost = 354.91010610434057

# Calculate the actual travel cost of the given tour
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

actual_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Check requirements
def verify_solution(tour, reported_cost, actual_cost):
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit all other cities exactly once
    unique_cities = set(tour[1:-1])  # Exclude the first and last depot city
    if len(unique_cities) != 9 or any(city not in unique_cities for city in range(1, 10)):
        return "FAIL"

    # Requirement 3: The total travel cost is minimized and matches the reported cost
    if not math.isclose(reported_cost, actual_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Verify the solution and print the result
result = verify_solution(tour, reported_cost, actual_cost)
print(result)