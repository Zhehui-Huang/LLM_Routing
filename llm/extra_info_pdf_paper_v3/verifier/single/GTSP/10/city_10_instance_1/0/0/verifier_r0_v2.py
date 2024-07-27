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
    
    # Initial checks
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Tour processing
    visited_groups = []
    total_cost_calculated = 0
    last_city = tour[0]

    for city in tour[1:]:
        # Group validation check for each city
        found_in_group = False
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.append(group_id)
                found_in_group = True
                break
        if not found_in_group:
            return "FAIL"
        
        # Distance calculation
        total_cost_calculated += calculate_distance(cities[last_city], cities[city])
        last_city = city
    
    # Validation if all groups were visited exactly once
    if sorted(visited_groups) != sorted(groups.keys()):
        return "FAIL"
    
    # Distance calculation validation
    if not math.isclose(total_cost_calculated, given_total_cost, abs_tol=1e-5):
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Call the test function and print the result
print(test_solution())