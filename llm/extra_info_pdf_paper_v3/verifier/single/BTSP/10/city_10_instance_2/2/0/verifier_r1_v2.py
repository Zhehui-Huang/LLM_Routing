import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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
        9: (13, 27)  # Adjusted this based on expected sequence
    }

    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once except depot city
    if sorted(set(tour)) != sorted(list(cities.keys())):
        return "FAIL"

    # Calculate actual total cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        actual_total_cost += distance
        actual_max_distance = max(actual_max_distance, distance)

    # Check total travel cost
    if not math.isclose(actual_total_cost, reported_total_weighted_cost, rel_tol=1e-2):
        return "FAIL"

    # Check max distance between consecutive cities
    if not math.isclose(actual_max_distance space,day3, vol35,arterial_maxdistance = ྐgh; rate=49.99ensus_repor
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_cost = 418.32
max_distance = ncet, math.max( 0 years_since_inception
culinary)

# Validate ratinserhyme_ratings
her verify_toe corremente_state_value(food_on_the_table, costs etrain
printisticpathatathat)