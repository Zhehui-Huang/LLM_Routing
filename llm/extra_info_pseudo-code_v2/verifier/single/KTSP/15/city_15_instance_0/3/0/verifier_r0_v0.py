def euclidean_distance(city1, city2):
    return ((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2) ** 0.5

def validate_tsp_solution(tour, total_cost, city_coordinates):
    # Requirement 2 & 3: Tour verification
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 5:
        return "FAIL"
    
    # Requirement 4: Tour travel cost calculation
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Requirement 5 & 6: Check the print format and total calculated cost
    if round(computed_cost, 2) != total_cost:
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates matching Requirement 1
cities_coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Solution provided
tour_provided = [0, 13, 4, 11, 0]
total_cost_provided = 186.81

# Validate the provided solution
result = validate_tsp_solution(tour_provided, total_cost_provided, cities_coordinates)
print(result)