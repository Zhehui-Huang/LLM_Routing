import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, travel_cost):
    # City coordinates
    coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
        5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
    }
    
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits all cities exactly once except depot city 0
    unique_cities = set(tour)
    if sorted(unique_cities) != list(range(0, 10)):
        return "FAIL"
    
    # Check calculated tour cost vs given tour cost
    calculated_cost = 0
    n = len(tour)
    for i in range(n - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    calculated_cost = round(calculated_cost, 2)

    if abs(calculated_cost - travel_cost) > 0.001:  # allowing very small floating point variations
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 0]
total_travel_cost = 242.74

# Verification
verification_result = verify_tour(tour, total_travel_cost)
print(verification_result)