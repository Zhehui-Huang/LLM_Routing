import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_cost):
    cities_coordinates = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # [Requirement 1] The robot must begin and end its tour at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The robot must visit exactly 8 out of the 10 cities listed, including the depot city.
    if len(set(tour)) != 9 or len(tour) != len(set(tour)):
        return "FAIL"
    
    # [Requirement 5] The output should be the list of city indices starting and ending at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total cost based on the tour provided and compare
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i-1]], cities_coordinates[tour[i]])
    
    # [Requirement 6] The output should also include the total travel cost of the tour.
    # Allowing a small margin for floating point comparison issues.
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    
    # If all checks passed:
    return "CORRECT"

# Provided test tour and cost
tour_test = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_cost_test = 235.38

# Validate solution
result = validate_solution(tour_test, total_cost_test)
print(result)