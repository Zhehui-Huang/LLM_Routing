import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Check if all cities are included, including the depot
    if len(cities) != 20:
        return "FAIL"
    
    # Check if the tour starts and ends at the depot city, and visits exactly 4 cities
    if len(tour) != 5 or tour[0] != 0 or tour[-1] != 0 or tour[1] != tour[-2]:
        return "FAIL"
    
    # Calculate the travel cost using the Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        total_cost += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    # Check if the calculated cost closely matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Define cities coordinates: [index: (x, y)]
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Provided solution details
tour = [0, 1, 8, 4, 0]
reported_cost = 110.09

# Verify the solution
print(verify_solution(cities, tour, reported_cost))