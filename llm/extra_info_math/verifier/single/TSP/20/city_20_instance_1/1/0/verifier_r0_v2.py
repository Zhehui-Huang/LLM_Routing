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
reported_cost = 357.73660855  # Corrected reported cost based on expected output from the given problem

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Verify Tour Starts and Ends at the Depot City (Requirement 1 and 10)
if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
    print("FAIL")
    exit()

# Verify All Cities Are Visited Exactly Once (Requirement 2, 7, 8)
unique_visited_cities = set(proposed_tour[1:-1])
if len(unique_visited_cities) + 1 != len(cities):
    print("FAIL")
    exit()

# Calculator total travel cost and check against reported (Requirements 5 and 6)
calculated_cost = sum(distance(proposed_tour[i], proposed_tour[i+1]) for i in range(len(proposed_tour) - 1))

# Check if calculated travel cost is close to the reported cost
if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-9):
    print("FAIL")
    exit()

# Check if each city is entered and left exactly once
if any(proposed_tour.count(city) != 1 for city in cities if city != 0):
    print("FAIL")
    exit()

# Pass all checks
print("CORRECT")