import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_cost):
    # Locations of cities
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must include exactly 13 cities (including depot)
    if len(tour) != 14 or len(set(tour)) != 14:
        return "FAIL"
    
    # Requirement 3 & 4: Calculate total cost and check with provided total cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1, city2 = tour[i], tour[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass:
    return "CORRECT"
    
# Example usage:
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
total_travel_duty = 273.7443523737762
print(verify_tour(tour, total_travel_duty))