import math

# Data for cities, given as (x, y) coordinates
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

# Example solution as derived from output (Here hardcoded sequence of city indices for illustration)
tour = [0, 1, 8, 5, 13, 17, 18, 3, 15, 11, 9, 12, 7, 14, 16, 4, 2, 6, 19, 10, 0]
expected_cost = 316.08092827

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute total travel cost from the tour
def compute_total_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i-1], tour[i])
    return total_cost

# Check if all cities are visited exactly once and tour starts and ends at depot city
def check_tour_validity(tour):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Check if each city from 1 to 19 is visited exactly once
    visited = set(tour[1:-1])  # Exclude the initial and final depot city
    if len(visited) != 19 or any(city not in visited for city in range(1, 20)):
        return False
    return True

# Validate solution
valid_tour = check_tour_validity(tour)
calculated_cost = compute_total_cost(tour)
cost_is_correct = math.isclose(calculated_cost, expected_cost, rel_tol=1e-9)

# Based on validations, determine if the result is correct
if valid_tour and cost_is_correct:
    print("CORRECT")
else:
    print("FAIL")