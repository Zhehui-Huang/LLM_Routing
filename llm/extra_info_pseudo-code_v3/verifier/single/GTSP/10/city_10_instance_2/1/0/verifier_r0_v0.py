import math

# Define the cities with their positions
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define the groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Proposed solution tour and its total cost
proposed_tour = [0, 3, 5, 9, 1, 2, 0]
reported_cost = 281.60273931778477

def calculate_distance(city_a, city_b):
    """Calculates Euclidean distance between two cities."""
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, groups):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly one city from each group
    visited_cities = tour[1:-1]  # Exclude the depot city from the list of visited cities
    for group in groups:
        if not any(city in group for city in visited_cities) or sum(city in group for city in visited_cities) != 1:
            return "FAIL"
    
    # Calculate the total cost of the tour and compare with the reported cost
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Allow small floating point differences in costs comparison
    if not math.isclose(calculated_cost, reported_difference, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Call the verification function and print the result
print(verify_tour(proposed_tour, groups))