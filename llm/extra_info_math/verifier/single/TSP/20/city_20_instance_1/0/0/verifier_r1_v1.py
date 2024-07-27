import math

# Given cities and their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Provided tour
tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]
reported_cost = 376.93470962470616

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cities, reported_cost):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour[1:-1]) != sorted([key for key in cities.keys() if key != 0]):
        return "FAIL"
    
    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check the cost matching
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Check and output the results
result = verify_tour(tour, cities, reported_cost)
print(result)  # Expected to print "CORRECT" if all checks are passed