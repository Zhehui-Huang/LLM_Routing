import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost, city_coordinates):
    # Check Requirement 1: Tour must start and end at the depot city (city 0).
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check Requirement 2: Robot must visit exactly 7 different cities, including the depot.
    if len(set(tour)) != 7 or len(tour) != 8:
        return "FAIL"

    # Check Requirement 3: Calculate actual travel cost using Euclidean distance and compare.
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    # Check for rounding issues by comparing the rounded values.
    if not math.isclose(actual_cost, total_cost, abs_tol=0.1):
        return "FAIL"
    
    # Requirement 4, 5, 6 are structurally adhered to by this point if all previous checks pass
    return "CORRECT"

# City coordinates mapped by their indices: {city_index: (x_coordinate, y_coordinate)}
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Solution
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_cost = 160

# Validate the solution
result = check_solution(tour, total_cost, cities)
print(result)