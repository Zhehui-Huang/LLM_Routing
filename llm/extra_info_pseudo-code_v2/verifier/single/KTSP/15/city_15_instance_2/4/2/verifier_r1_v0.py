import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(cities, tour, total_cost):
    # Check if tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 unique cities are visited
    if len(set(tour)) != 9:  # includes the depot visited twice
        return "FAIL"
    
    # Check if cities in tour are valid
    if any(city not in range(len(cities)) for city in tour):
        return "FAIL"
    
    # Calculate total distance of the provided tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += compute_euclidean_distance(cities[city1][0], cities[city1][1],
                                                      cities[city2][0], cities[city2][1])

    # Compare calculated distance with provided total distance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Defined cities with their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Provided tour and total cost
tour = [0, 14, 1, 12, 3, 9, 13, 2, 0]
total_cost = 248.24

# Validate the given solution and conditions
result = verify_tour(cities, tour, total_cost)
print(result)