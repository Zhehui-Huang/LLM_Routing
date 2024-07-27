import math

# City coordinates
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

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tsp(tour, expected_cost):
    """ Verify the conditions of the TSP problem """
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited = set(tour)
    # Remove the depot city which is allowed to be visited twice (start, end)
    if 0 in visited:
        visited.remove(0)
    if len(visited) != len(cities) - 1:
        return "FAIL"
    
    # Check the total cost calculation
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 2, 0]
total_travel_cost = 30.59  # Provided cost

# Verify and print the result
result = verify_tsp(tour, total_travel_cost)
print(result)