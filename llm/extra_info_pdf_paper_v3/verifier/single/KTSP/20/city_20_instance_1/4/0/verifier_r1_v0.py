import math

# Coordinates of cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Proposed solution
tour = [0, 6, 2, 13, 8, 9, 14, 0]
reported_cost = 130.67

def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, expected_cities_count):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly 7 cities are visited, including the depot
    if len(set(tour)) != expected_cities_count:
        return False
    
    return True

def verify_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_distance(tour[i], tour[i + 1])
    return total_cost

# Test the tour
if verify_tour(tour, 7):
    calculated_cost = verify_travel_cost(tour)
    # Allow small precision errors in floating point arithmetic
    if abs(calculated_cost - reported_cost) < 1e-2:
        print("CORRECT")
    else:
        print("FAIL")
else:
    print("FAIL")