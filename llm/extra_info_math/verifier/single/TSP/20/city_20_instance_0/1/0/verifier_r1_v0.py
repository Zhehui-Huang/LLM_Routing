import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, cities_coordinates, reported_cost):
    # Check starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check visits each other city exactly once
    visited = set(tour[1:-1])  # Exclude the depot start/end
    if len(visited) != 19 or any(city not in visited for city in range(1, 20)):
        return "FAIL"

    # Calculate total travel cost based on the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        x1, y1 = cities_coordinates[city_from]
        x2, y2 = cities_coordinates[city_to]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if computed travel cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of each city
cities_coordinates = [
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

# Provided solution to verify
tour = [0, 4, 1, 0, 4, 1, 0, 4, 1, 0, 4, 1, 0, 4, 1, 0, 4, 1, 0, 4, 0]
reported_cost = 316.08

# Validate the solution
result = validate_tour(tour, cities_coordinates, reported_cost)
print(result)