import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, coordinates):
    # Constants
    REQUIRED_CITY_COUNT = 5
    
    # Check starting and ending at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the tour visits exactly 5 cities
    if len(tour) != REQUIRED_CITY_COUNT + 1:
        return "FAIL"
    
    # Check all cities are visited once except depot
    if len(set(tour)) != REQUIRED_CITY_COUNT:
        return "FAIL"
    
    # Check city indices are within the valid range
    if any(city < 0 or city > 9 for city in tour):
        return "FAIL"
    
    # Check travel cost calculation
    # Given total cost
    given_total_cost = 110.38072506104011

    # Calculated total cost
    calculated_total_cost = sum(
        calculate_distance(coordinates[tour[i]][0], coordinates[tour[i]][1], 
                           coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
        for i in range(len(tour) - 1)
    )

    # Allow for a small numeric discrepancy in floating point arithmetic
    if not math.isclose(given_total_cost, calculated_total_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates as provided in the description
city_coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Proposed solution tour and cost
tour = [0, 4, 8, 3, 5, 0]

# Validation call
validation_result = validate_tour(tour, city_coordinates)
print(validation_result)