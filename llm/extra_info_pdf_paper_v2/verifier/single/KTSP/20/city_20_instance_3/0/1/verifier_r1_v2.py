import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_cost):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
        (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
        (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
        (53, 76), (19, 72)
    ]

    # Check if the start and end are at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 13 cities are visited
    if len(tour) != 14:  # including the repetition of the depot city
        return "FAIL"
    
    # Ensure all city indices in the tour are valid
    if any(city < 0 or city >= len(cities) for city in tour):
        return "FAIL"

    # Calculate the total travel cost and compare it with the given total cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])

    # Check if the reported total cost is correct up to two decimal places
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Define the correct test variables
tour_solution = [0, 3, 19, 6, 2, 13, 18, 16, 10, 4, 14, 8, 7, 0]
total_cost_solution = 383.16

# Test the given solution
print(validate_solution(tour_solution, total_cost_solution))