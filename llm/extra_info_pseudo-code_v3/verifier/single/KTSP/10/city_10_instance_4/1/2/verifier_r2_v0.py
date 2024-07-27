import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost):
    # Cities coordinates
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
    
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities are visited, including the depot
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Check if tour only contains cities from the given set
    if any(city not in cities for city in tour):
        return "FAIL"
    
    # Calculate the travel cost of the tour and validate it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - cost) > 1e-2:
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
best_tour = [0, 1, 5, 7, 9, 3, 4, 0, 0]
best_tour_cost = 178.11

# Validate the solution
result = verify_solution(best_tour, best_tour_cost)
print(result)