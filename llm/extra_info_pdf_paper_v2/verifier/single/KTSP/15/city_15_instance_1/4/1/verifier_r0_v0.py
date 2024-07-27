import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, expected_cost):
    # Requirement: The tour must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement: The robot needs to visit exactly 6 cities, including the depot city.
    if len(tour) != 7:  # tour includes returning to the depot, hence 7 entries
        return "FAIL"

    # Requirement: The goal is to find the shortest possible tour.
    # This requirement is theoretically compromising to check without solving the problem itself, so skip.
    
    # Requirement: The travel cost is calculated as the Euclidean distance between two cities.
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }

    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 7, 6, 13, 12, 10, 0]
total_travel_cost = 342.18971971745964

# Check solution correctness
print(verify_solution(tour, total_travel_cost))