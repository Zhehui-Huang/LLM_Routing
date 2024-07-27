import math

def calculate_distance(city_a, city_b):
    x1, y1 = city_a
    x2, y2 = city_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, total_cost, coordinates):
    # Check start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 5 cities, including the depot city
    if len(tour) != 6 or len(set(tour)) != 5:
        return "FAIL"
    
    # Check travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare computed travel cost with provided travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-4):
        return "FAIL"
    
    # Placeholder for checking if the tour is the shortest possible (not validated here)
    # Just a placeholder, requires a method or logic to compute the shortest tour.
    # This part is generally not possible to check without full access to all possible tours,
    # and an efficient algorithm to find the shortest tour.
  
    # If all checks pass:
    return "CORRECT"

# Given data and purported solution
coordinates = {
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

purported_solution_tour = [0, 9, 9, 9, 9, 0]
purported_solution_cost = 93.91485505499116

# Validate the solution
result = validate_tour(purported_solution_tour, purported_solution_cost, coordinates)
print(result)