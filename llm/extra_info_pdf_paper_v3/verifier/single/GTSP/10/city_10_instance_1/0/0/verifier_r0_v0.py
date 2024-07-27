import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def test_solution():
    # Cities and their coordinates
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    # Groups of cities
    groups = {
       0: [5, 6, 7],
       1: [2, 3],
       2: [1, 9],
       3: [4, 8]
    }

    # Given tour
    tour = [0, 9, 5, 3, 8, 0]
    
    # Given total cost
    given_total_cost = 169.9409598467532

    # Test if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    visited_groups = []
    total_cost_calculated = 0

    # Test if the tour visits exactly one city from each group and calculate the actual tour distance
    last_city = tour[0]
    for city in tour[1:]:
        # Check if the city is found in exactly one group
        found_in_group = False
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.append(group_id)
                found_in_group = True
                break
        if not found_in_static:
            return "FAIL"
        # Calculate the distance
        total_cost_calculated += calculate_distance(cities[last_city], cities[city])
        last_city = city

    # Check if all groups are visited exactly once
    if sorted(visited_groups) != sorted(groups.keys()):
        return "FAIL"

    # Check if the calculated tour cost matches the given tour cost with a tolerance for floating-point arithmetic
    if not math.isclose(total_cost_calculated, given_total_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

print(test_solution())