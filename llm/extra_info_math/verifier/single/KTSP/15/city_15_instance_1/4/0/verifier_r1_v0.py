import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour_solution(tour, total_cost, city_coordinates):
    # Requirement 1: Start and End at Depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Visit exactly 6 cities including the depot
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Requirement 3: Check if the total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates (depot city included)
cities_coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Solution to check
tour_solution = [0, 6, 1, 7, 3, 9, 0]
total_travel_cost_solution = 118.8954868377263

# Output verification result
result = validate_tour_solution(tour_solution, total_travel_cost_solution, cities_coordinates)
print(result)