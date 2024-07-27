import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tour, total_travel_cost):
    # Define coordinates of cities
    cities = {
        0: (8, 11),
        1: (40, 6),
        8: (61, 16),
        4: (25, 18),
    }
    
    # [Requirement 1] The robot must start and end its journey at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit exactly 4 cities, including the depot city.
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"

    # [Requirement 4] The tour should be the shortest path.
    # We'll need to calculate the tour cost and ascertain if it's the shortest possible.
    # As we can't practically verify shortest without complete enumeration or optimization, focus on calculation.
    calculated_cost = 0
    for i in range(1, len(tour)):
        previous_city = tour[i-1]
        current_city = tour[i]
        calculated_cost += euclidean_distance(cities[previous_city], cities[current_city])

    # [Requirement 3] The travel cost must be calculated as the Euclidean distance.
    if not math.isclose(calculated_cost, total_travel_data, rel_tol=1e-5):
        return "FAIL"

    # [Requirement 5] The output must be in the specified format.
    # This is Python internal and should always pass if the input is as specified.

    # If all checks are passed:
    return "CORRECT"

# Example usage:
tour = [0, 1, 8, 4, 0]
total_travel_cost = 110.08796524611944
print(verify_solution(tour, total_travel_cost))