import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, cities):
    # Requirement: The robot starts and ends the tour at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement: The robot must visit exactly 8 cities, including the depot city
    if len(tour) != 9:  # Includes return to the starting city
        return "FAIL"

    # Requirement: Check if all cities in the tour are unique except the starting and ending one
    if len(set(tour)) != 9:
        return "FAIL"
    
    # Requirement: Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement: Output the total travel cost of the tour
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):  # Accept slight precision differences
        return "FAIL"

    return "CORRECT"

# City coordinates (index corresponds to city number)
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

# Solution provided (tour and total travel cost)
tour = [0, 4, 7, 5, 1, 2, 6, 3, 0]
total_travel_cost = 301.21

# Verify the solution
result = verify_solution(tour, total_travel_cost, cities)
print(result)