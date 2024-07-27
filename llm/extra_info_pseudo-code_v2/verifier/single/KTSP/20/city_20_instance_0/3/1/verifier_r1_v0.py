import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def verify_solution(tour, total_travel_cost):
    # Coordinates for the depot and the cities
    coordinates = [
        (8, 11),   # Depot city 0
        (40, 6),   # City 1
        (95, 33),  # City 2
        (80, 60),  # City 3
        (25, 18),  # City 4
        (67, 23),  # City 5
        (97, 32),  # City 6
        (25, 71),  # City 7
        (61, 16),  # City 8
        (27, 91),  # City 9
        (91, 46),  # City 10
        (40, 87),  # City 11
        (20, 97),  # City 12
        (61, 25),  # City 13
        (5, 59),   # City 14
        (62, 88),  # City 15
        (13, 43),  # City 16
        (61, 28),  # City 17
        (60, 63),  # City 18
        (93, 15)   # City 19
    ]

    # Check requirements
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city 0."

    if len(tour) != 5:  # including the returning to depot city
        return "FAIL", "The robot does not visit exactly 4 cities."

    if calculate_total_travel_factor(tour, coordinates) != total_travel_cost:
        return "FAIL", "Total travel cost does not match computed cost."

    if any(tour.count(city) > 1 for city in tour if city != 0):
        return "FAIL", "A city is visited more than once (excludes depot city)."

    # Since we cannot verify the actual use of GVNS algorithm (Requirement 4) via unit test, we shall omit it.
    return "CORRECT", "All requirements met."

# Example Solution    
tour_example = [0, 1, 8, 4, 0]
total_travel_cost_example = 110.08796524611944

# Verification Call
result, message = verify_solution(tour_example, total_travel_cost_example)
print(result)