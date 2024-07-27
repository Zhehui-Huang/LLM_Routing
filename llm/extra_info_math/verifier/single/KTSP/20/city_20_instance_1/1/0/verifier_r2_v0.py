import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    # Requirement 1: Check if exactly 7 cities, including the depot, are visited
    if len(tour) != 8 or len(set(tour)) != 8:  # Tour should include exactly 7 + 1 repeated depot city
        return "FAIL"

    # Requirement 2: Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total distance of the provided tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Provided total travel cost
    provided_cost = 130.6658168109853

    # Requirement 3: Check the distance calculation matches the provided distance (with some margin for error due to floating-point arithmetic)
    if not math.isclose(total_distance, provided_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Cities coordinates
cities = [
    (14, 77),  # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9),
]

# Solution to verify
solution_tour = [0, 6, 2, 13, 8, 9, 14, 0]

# Verify solution
print(verify_solution(solution_tour, cities))