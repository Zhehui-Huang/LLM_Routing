import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cost):
    cities = {
        0: (3, 26),
        1: (85, 72),
        2: (67, 0),
        3: (50, 99),
        4: (61, 89),
        5: (91, 56),
        6: (2, 65),
        7: (38, 68),
        8: (3, 92),
        9: (59, 8),
        10: (30, 88),
        11: (30, 53),
        12: (11, 14),
        13: (52, 49),
        14: (18, 49),
        15: (64, 41),
        16: (28, 49),
        17: (91, 94),
        18: (51, 58),
        19: (30, 48)
    }
    
    # Verify the number of unique cities (including the depot city)
    if len(set(tour)) != 10 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the total travel cost from the provided tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])

    # Compare calculated cost to provided cost
    if abs(calculated_cost - cost) > 1e-2:  # allowing a small error margin
        return "FAIL"
    
    return "CORRECT"

# Provided tour solution
tour = [0, 12, 9, 2, 15, 1, 18, 11, 16, 14, 0]
cost = 252.95014228363397
result = verify_tour(tour, cost)
print(result)