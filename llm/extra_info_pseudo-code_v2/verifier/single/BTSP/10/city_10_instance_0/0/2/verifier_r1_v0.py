import math
from collections import defaultdict

# Given data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Solution provided
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_cost_provided = 295.99
max_distance_provided = 56.46

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_properties(tour, cities):
    # Check if tour starts and ends at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour must start and end at city 0"
    
    # Check if each city is visited exactly once, except for the depot city
    unique_visits = set(tour)
    if len(unique_visits) != len(cities) or sorted(unique_visits) != sorted(cities.keys()):
        return "FAIL", "Tour must visit each city exactly once"

    # Calculate the total cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        c1 = tour[i]
        c2 = tour[i + 1]
        distance = calculate_euclidean_distance(cities[c1][0], cities[c1][1], cities[c2][0], cities[c2][1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check the total tour cost and max distance with provided solution properties
    if not math.isclose(total_cost, total_cost_provided, rel_tol=1e-2):
        return "FAIL", f"Provided total cost ({total_cost_provided}) does not match calculated cost ({total_cost:.2f})"
    if not math.isclose(max_distance, max_distance_provided, rel_tol=1e-2):
        return "FAIL", f"Provided max distance ({max_distance_provided}) does not match calculated max distance ({max_distance:.2f})"

    return "CORRECT", None

# Verify the solution
result, error_message = verify_tour_properties(tour, cities)
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL: " + error_message)