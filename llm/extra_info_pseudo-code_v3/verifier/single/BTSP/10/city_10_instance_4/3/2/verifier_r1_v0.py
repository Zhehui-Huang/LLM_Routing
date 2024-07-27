import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(solution):
    # City coordinates
    cities = {
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
    
    # Unpacking the solution
    tour, total_travel_cost, max_distance = solution['Tour'], solution['Total travel cost'], solution['Maximum distance between consecutive cities']
    
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city visited exactly once
    if len(tour) != len(cities) + 1 or set(tour) != set(cities.keys()).union({0}):
        return "FAIL"
    
    # Check Requirement 4: Tour includes the list starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the actual travel cost and max distance through the tour
    calculated_cost = 0
    calculated_max_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
            
    # Check Requirement 5: Total travel cost is correct
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 6: Maximum distance is correct
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=0.01):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

solution = {'Tour': (0, 6, 3, 1, 4, 5, 7, 9, 8, 2, 0), 'Total travel cost': 465.16, 'Maximum distance between consecutive cities': 99.25}
result = check_solution(solution)
print(result)