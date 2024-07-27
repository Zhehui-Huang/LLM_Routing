import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, expected_cost):
    # [Requirement 1] Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 3 additional cities are visited
    if len(tour) != 5:  # Includes start and end at depot city
        return "FAIL"
    
    # [Requirement 3] Check if the path has the shortest possible total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all requirements are met
    return "CORRECT"

# Coordinates of the cities (index corresponds to city number)
cities = [
    (8, 11),  # Depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15),
]

# Provided solution
tour = [0, 1, 4, 16, 0]
reported_total_cost = 111.72

# Verify if provided tour and cost are correct
result = verify_tour(cities, tour, reported_total_cost)
print(result)