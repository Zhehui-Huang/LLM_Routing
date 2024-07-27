import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, city_coordinates):
    # [Requirement 2] Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city."
    
    # [Requirement 1] Check if all cities are visited exactly once, excluding the depot city
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(city_coordinates) - 1 or not all(city in unique_cities for city in range(1, len(city_coordinates))):
        return "FAIL: Not all cities are visited exactly once."
    
    # [Requirement 4] Check format of the tour (implicitly checked by inputs, no specific format error can occur in a well-defined list)
    
    # Calculating total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        total_cost += calculate_distance(x1, y1, x2, y2)
    
    # [Requirement 3] and [Requirement 5] are implicitly checked and outputted in the process
    return total_cost

# Define city coordinates as given
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Provided tour
provided_tour = [0, 14, 16, 19, 11, 7, 10, 3, 4, 1, 17, 5, 2, 9, 15, 13, 18, 8, 6, 12, 0]
provided_cost = 492.2863052323856

# Verify tour and cost
calculated_cost = verify_tour(provided_tour, cities)
if abs(calculated_cost - provided_cost) < 1e-6:  # Allowing a small error margin for floating point calculations
    print("CORRECT")
else:
    print(f"FAIL: Calculated cost {calculated_cost} does not match provided cost {provided_cost}.")