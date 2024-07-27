import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_cost_calculated):
    cities_coordinates = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # Check if tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited, including the depot
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate total travel cost and compare with the provided cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities_coordinates[city1]
        x2, y2 = cities_coordinates[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # The total cost should be approximately equal to the calculated total cost
    if not math.isclose(total_cost, total_cost_calculated, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Example tour and total travel cost provided
tour_example = [0, 1, 10, 8, 0]
total_travel_cost_example = 90.53947981328088

# Verify the solution
result = verify_tour(tour_example, total_travel_cost_example)
print(result)  # Output should be "CORRECT" if everything is validated correctly