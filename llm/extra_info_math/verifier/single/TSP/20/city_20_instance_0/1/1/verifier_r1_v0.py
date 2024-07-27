import math

# List of cities with their coordinates
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

# Optimal tour obtained from the solution
optimal_tour = [0, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 2, 6, 19, 5, 17, 13, 8, 1, 4, 0]
optimal_cost = 349.2

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, expected_cost):
    # Check if the start and end city are the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once except the depot
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(tour.count(city) != 1 for city in cities if city != 0):
        return "FAIL"

    # Calculate the cost and check it against optimal
    total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if abs(total_cost - expected_cost) > 0.1:  # small error tolerance
        return "FAIL"

    # Check subtour elimination implicitly by verifying tour loop criteria.
    # Detailed subtour elimination is handled algorithmically via solver constraints.

    return "CORRECT"

# Print checking results
result = verify_tour(optimal_tour, optimal_cost)
print(result)