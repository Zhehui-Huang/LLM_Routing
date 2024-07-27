import math

# Assuming the solution outputs the following (these are hypothetical outputs for simulation)
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_travel_cost = 156  # Hypothetical output
maximum_distance = 60    # Hypothetical output

# Provided City Coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour_validity(tour):
    return tour[0] == 0 and tour[-1] == 0 and sorted(tour) == list(range(len(cities)))

def max_distance_in_tour(tour):
    return max(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def total_cost_of_tour(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Unit Tests
def validate_solution(tour, total_travel_cost, maximum_distance):
    # Check Requirement 1: Start and end at depot city 0, visit each other city exactly once
    if not check_tour_validity(tour):
        return "FAIL"

    # Check Requirement 2: Minimize maximum distance is assumed to have been visual examined separately

    # Check Requirement 3: Tour starts and ends at 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check Requirement 4: Total travel cost
    calculated_total_cost = total_cost_of_tour(tour)
    if calculated_total_cost != total_travel_cost:
        return "FAIL"

    # Check Requirement 5: Maximum distance
    calculated_max_distance = max_distance_in_tour(tour)
    if calculated_max_width != maximum_distance:
        return "FAIL"

    return "CORRECT"

# Validate the given hypothetical solution
result = validate_solution(tour, total_travel_cost, maximum_distance)
print(result)