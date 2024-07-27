import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coords):
    # Defined constraints
    VISITED_CITIES_COUNT = 4
    DEPOT_CITY = 0

    # Check for exactly 4 cities including the depot
    if len(tour) != 5 or tour[0] != DEPOT_CITY or tour[-1] != DEPOT_CITY:
        return "FAIL"
    
    # Check all cities are valid
    unique_cities = set(tour)
    if not all(city in range(len(city_coords)) for city in unique_cities):
        return "FAIL"
    
    # Check actual travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*city_coords[city_from], *city_coords[city_to])
    
    calculated_cost = round(calculated_cost, 2)  # Round the cost for precision handling
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities in the format: city_index: (x, y)
city_coords = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Solution provided
tour = [0, 1, 8, 4, 0]
total_cost = 110

# Check the solution
print(verify_solution(tour, total_cost, city_coords))