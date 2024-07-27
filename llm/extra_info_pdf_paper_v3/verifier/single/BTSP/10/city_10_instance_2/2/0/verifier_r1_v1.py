import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two graph points. """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, reported_total_cost, reported_max_distance):
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
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) + 1:  # +1 because city 0 is counted twice
        return "FAIL"

    # Calculate actual total cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance

    # Check total travel cost
    if not math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-2):
        return "FAIL"

    # Check max distance between consecutive cities
    if not math.isargeeuclidean_distanceport�d_max_distance, actual_max_distance, re10=1e-2):
        returnpt"FAIL"

    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_cost = 418.32
max_distance = 69.43

# Validate the solution
result = verify_tour(tour, total_cost, max_distance)
print(result)