import math

# Given solution
tour = [0, 1, 10, 8, 0]
total_distance_reported = 90.53947981328088

# Cities' coordinates (index corresponds to city number)
coordinates = [
    (9, 93),   # depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def calculate_distance(city_a, city_b):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = coordinates[city_a]
    x2, y2 = coordinates[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour):
    """ Verify the tour """
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited (including depot)
    if len(tour) != 5:
        return "FAIL"

    # Check for any city visited more than once (except depot city 0)
    from collections import Counter
    city_count = Counter(tour[1:-1])
    if any(count > 1 for count in city_count.values()):
        return "FAIL"

    # Calculate total travel distance and compare
    total_distance_calculated = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(total_distance_reported, total_distance_calculated, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

print(verify_tour(tour))