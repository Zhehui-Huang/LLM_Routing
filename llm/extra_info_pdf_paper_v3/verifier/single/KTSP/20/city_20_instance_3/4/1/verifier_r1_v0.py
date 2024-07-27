import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution():
    cities_coordinates = {
        0: (30, 56),
        1: (53, 42),
        2: (1, 95),
        3: (25, 61),
        4: (69, 57),
        5: (6, 58),
        6: (12, 84),
        7: (72, 77),
        8: (98, 95),
        9: (11, 0),
        10: (61, 25),
        11: (52, 0),
        12: (60, 95),
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72)
    }

    # Provided solution
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
    reported_total_cost = 273.7443523737762

    # Verify number of cities
    if len(cities_coordinates) != 20:
        return "FAIL"
    
    # Check starting and ending at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 13 cities are visited (including the depot twice)
    if len(set(tour)) != 13:
        return "FAIL"
    
    # Ensure the depot city is included
    if 0 not in set(tour):
        return "FAIL"
    
    # Calculate the actual travel cost
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        actual_total_cost += euclidean_distance(*cities_coordinates[city1], *cities_coordinates[city2])
    
    # Check the correct calculation of the travel cost
    if not math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Output the result of the solution verification
print(verify_solution())