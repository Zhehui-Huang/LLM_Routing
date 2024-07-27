import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    if len(city_coordinates) != 20:
        return "FAIL"  # Check for correct number of cities
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check tour starts and ends at the depot city 0
    
    if len(set(tour)) != len(city_coordinates) or set(tour) != set(range(len(city_coordinates))):
        return "FAIL"  # Check all cities are visited exactly once
    
    # Compute the total travel cost from the tour for verification
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    if not (math.isclose(calculated_cost, total_cost, rel_tol=1e-9)):
        return "FAIL"  # Check if provided cost matches calculated cost
    
    # If all checks pass, assume solution is correct
    return "CORRECT"

# Coordinates for the cities, from City 0 to City 19
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Tour and the total cost provided
tour_provided = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_cost_provided = 458.37

# Verify the solution
result = verify_solution(tour_provided, total_cost_provided, city_coordinates)
print(result)