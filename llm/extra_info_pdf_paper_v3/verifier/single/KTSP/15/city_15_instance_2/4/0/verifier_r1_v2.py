import math

# Positions of cities
city_positions = {
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
    14: (6, 99),
}

# Given tour and its reported cost
provided_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
reported_cost = 132.12

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.hypot(x2 - x1, y2 - y1)

def test_tour():
    # Check the tour starts and ends at the depot city
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities, including the depot, are visited
    if len(set(provided_tour)) != 8:
        return "FAIL"
    
    # Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(provided_tour) - 1):
        total_cost += calculate_distance(provided_tour[i], provided_tour[i + 1])
    
    # Check if the calculated cost is close to the reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Perform the test and print the result
test_result = test_tour()
print(test_result)