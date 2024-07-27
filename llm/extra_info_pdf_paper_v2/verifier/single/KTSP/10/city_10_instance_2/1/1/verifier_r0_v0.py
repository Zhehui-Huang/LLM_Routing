import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def unit_test_tour_and_cost(tour, cost):
    city_coords = [
        (90, 3),  # Depot city 0
        (11, 17),
        (7, 27),
        (95, 81),
        (41, 54),
        (31, 35),
        (23, 95),
        (20, 56),
        (49, 29),
        (13, 17)
    ]
    
    # Check requirement: The robot must visit exactly 6 cities, including the depot city (city 0 and it must start and end at depot city 0).
    if len(set(tour)) != 6 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement: The tour must start and end at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel cost using Euclidean distance and check requirement.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coords[tour[i]]
        x2, y2 = city_coords[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if provided cost is correctly calculated
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided test solution
tour_test = [0, 9, 1, 2, 5, 8, 0]
total_travel_cost_test = 105.59116123237973

# Call the unit testing function and print the result
print(unit_test_tour_and_cost(tour_test, total_travel_cost_test))