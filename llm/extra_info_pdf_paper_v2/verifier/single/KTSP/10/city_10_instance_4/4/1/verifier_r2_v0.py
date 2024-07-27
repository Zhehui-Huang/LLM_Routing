import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    # Requirement: The robot should start and end its journey at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement: Exactly 8 cities, including the depot city, must be visited
    if len(set(tour)) != 8:
        return "FAIL"

    # Requirement: The output should be a list of city indices, starting and ending at depot city 0
    if not all(isinstance(city, int) for city in tour):
        return "FAIL"

    # Calculate traveled distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement: Check approximate total cost with a small tolerance due to floating-point arithmetic
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"


# Definition of cities coordinates {city_index: (x, y)}
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

# Solution provided
tour_output = [0, 1, 5, 7, 9, 8, 3, 4, 0]
total_travel_cost_output = 286.8833289162046

# Function call to validate the output
result = verify_solution(tour_output, total_travel_data_output, cities)
print(result)