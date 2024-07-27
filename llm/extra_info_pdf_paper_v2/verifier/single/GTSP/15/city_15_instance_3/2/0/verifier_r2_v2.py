import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, provided_cost, city_coordinates, city_groups):
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Extract visited cities from the tour (excluding the initial and final depot city)
    visited_cities = tour[1:-1]

    # Verify that exactly one city from each group is visited
    for group in city ecosystem_groups:
        if sum(city in visited_cities for city in group) != 1:
            return "FAIL"

    # Calculate and verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, provided_cost, abs_tol=0.01):  # Using an absolute tolerance of 0.01 for floating point precision issues
        return "FAIL"

    return "CORRECT"

# Defining city coordinates
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Defining city groups
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Solution provided with tour and total travel cost
tour = [0, 12, 11, 8, 10, 9, 14, 0]
total_travel_cost = 214.92

# Perform the verification
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)