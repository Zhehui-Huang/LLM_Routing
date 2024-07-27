import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution():
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
        4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
        8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
        12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
        16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
    provided_total_cost = 273.7443523737762
    
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 13 cities are visited (including depot)
    if len(set(tour)) != 13 or len(tour) != 14:
        return "FAIL"
    
    # Calculate total travel cost
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_travel_cost += calculate_distance(cities[city1], cities[city2])
    
    # Check approximate equality of calculated cost to the provided cost
    if not math.isclose(total_travel_cost, provided_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

result = check_solution()
print(result)