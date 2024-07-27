import math

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of the cities in the tour (adjusted to only include cities within the tour)
    cities = {
        0: (8, 11),
        1: (40, 6),
        4: (25, 18),
        8: (61, 16),
    }

    # Requirement 1: The robot must start and end its journey at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: The robot must visit exactly 4 cities, including the depot city.
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"

    # Calculating the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 3: The travel cost must be calculated as the Euclidean distance, and must match the given cost.
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed:
    return "CORRECT"

# Example usage
tour = [0, 1, 8, 4, 0]
total_travel_cost = 110.08796524611944
print(verify_solution(tour, total_travel_cost))  # Should print "CORRECT" if all requirements are met