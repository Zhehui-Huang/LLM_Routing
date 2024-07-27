import math

# Input coordinates for each city
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
    4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
    8: (85, 71), 9: (6, 76)
}

# Solution to verify
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_travel_cost = 555.33
max_distance_consecutive_cities = float('inf')  # As given in the solution

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour):
    """ Validate the tour based on the given requirements """
    # Verify Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: Each city is visited exactly once
    visited = set(tour)
    expected = set(cities.keys())
    if visited != expected or len(tour) != len(visited):
        return "FAIL"

    # Verify Requirement 3: Minimize the longest distance between any two consecutive cities
    actual_max_distance = 0
    total_cost_computed = 0
    for i in range(len(tour) - 1):
        d = calculate_distance(tour[i], tour[i+1])
        total_cost_computed += d
        if d > actual_max_distance:
            actual_max_distance = d
    
    if not math.isclose(total_cost_computed, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if actual_max_distance != max_distance_consecutive_cities:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = validate_tour(tour)
print(result)