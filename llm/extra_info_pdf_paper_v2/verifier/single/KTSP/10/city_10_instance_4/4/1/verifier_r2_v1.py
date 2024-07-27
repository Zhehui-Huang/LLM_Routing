import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    # Requirement: Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement: Checks if exactly 8 distinct cities are visited, including the depot city
    if len(tour) != 9 or len(set(tour)) != 9:
        return "FAIL"

    # Requirement: Check if all values in the tour are valid city indices
    if not all(city in cities for city in tour):
        return "FAIL"

    # Calculate the total cost of travel based on the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement: Compare the calculated total travel cost with provided cost using a tolerance
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"


# City coordinates {city_index: (x, y)}
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

# Provided solution to verify
tour_output = [0, 1, 5, 7, 9, 8, 3, 4, 0]
total_travel_cost_output = 286.8833289162046

# Validate the output using the verification function
result = verify_solution(tour_output, total_travel_cost_output, cities)
print(result)  # Should print "CORRECT" if the solution and its cost are valid according to the specifications