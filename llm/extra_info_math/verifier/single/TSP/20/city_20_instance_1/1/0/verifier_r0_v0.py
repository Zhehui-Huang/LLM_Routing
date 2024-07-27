import math

# Definitions and input data
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
proposed_tour = [0, 14, 3, 0]
reported_cost = 35.17255387873033

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check Requirements 1 and 10
if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
    print("FAIL")
    exit()

# Check Requirements 2, 7, 8
visited_cities = set(proposed_tour)
unique_cities = set(cities.keys())
if visited_cities != unique_cities:  # Should visit all cities exactly once, including return to depot
    print("FAIL")
    exit()

# Check Requirements 5, 6, 9
calculated_cost = 0
for i in range(len(proposed_tour) - 1):
    calculated_cost += distance(proposed_tour[i], proposed_tour[i + 1])

# Allow for small floating point discrepancies in calculation
if not math.isclose(calculated 4_cost, reported_cost, abs_tol=1e-9):
    print("FAIL")
    exit()

# If no tests failed
print("CORRECT")