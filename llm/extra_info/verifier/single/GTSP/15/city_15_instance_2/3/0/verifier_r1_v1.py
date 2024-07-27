import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates for each city (including the depot city 0)
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
    
    # Group mapping
    city_groups = {
        0: [8, 12, 14],
        1: [7, 10, 11],
        2: [4, 6, 9],
        3: [1, 3, 13],
        4: [2, 5]
    }

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    unique_groups = set()
    for city_index in tour[1:-1]:  # scan through cities in the tour excluding the depot
        is_in_group = False
        for group, cities_in_group in city_groups.items():
            if city_index in cities_in_group:
                if group in unique_groups:
                    return "FAIL"  # city from the same group visited more than once
                unique_inc_group = True
                unique_groups.add(group)
                break
        if not is_in_group:
            return "FAIL"  # city in the tour is not in any group or double counting group cities
    if len(unique_groups) != 5:
        return "FAIL"

    # [Requirement 3 and 5]
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        computed_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])

    if abs(computed_cost - total_travel_cost) > 1e-6:  # Allow for some floating point tolerance
        return "FAIL"

    return "CORRECT"

# Given solution to verify
tour = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost = 138.15244358342136

# Check if the solution meets the requirements
print(verify_solution(tour, total_travel_cost))