import math

# City coordinates
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

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Provided solution details
tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 15, 19, 18, 2, 8, 12, 1, 13, 9, 6, 0]
total_cost = 443.69753810251024
max_distance = 32.57299494980466

# Verify each city is visited exactly once and returns to depot
if sorted(tour) == sorted(list(cities.keys()) + [0]):
    print("City Visit Check: PASS")
else:
    print("City Visit Check: FAIL")
    exit()

# Verify objective of minimizing the longest distance
calculated_distances = []
for i in range(len(tour)-1):
    distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_distances.append(distance)

# Verify if the maximum distance reported matches the expected output
if not math.isclose(max(calculated_distances), max_distance, abs_tol=0.0001):
    print("Maximum Distance Check: FAIL")
    exit()

# Calculate the total travel cost from the tour and verify
calculated_total_cost = sum(calculated_distances)
if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.0001):
    print("Total Travel Cost Check: FAIL")
    exit()

# If all checks are passed
print("CORRECT")