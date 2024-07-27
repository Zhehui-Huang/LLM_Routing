import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, total_cost_calc):
    # Cities coordinates indexed by their numbers
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # City groups
    city_groups = {
        0: [1, 2, 5, 6],
        1: [8, 9, 10, 13],
        2: [3, 4, 7],
        3: [11, 12, 14]
    }
    
    # Check [Requirement 1]: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check [Requirement 2]: One city from each group
    visited_groups = {key: False for key in city_groups}
    for city_index in tour[1:-1]:  # ignore the depot at start and end
        found_group = False
        for group_index, cities_in_group in city_groups.items():
            if city_index in cities_in_group:
                if visited_groups[group_index]:
                    return "FAIL"
                visited_groups[group_index] = True
                found_group = True
        if not found_group:
            return "FAIL"
    if not all(visited_groups.values()):
        return "FAIL"

    # Check [Requirement 3] and calculate total distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check [Requirement 4]: Correct total cost
    if not math.isclose(calculated_cost, total_cost_calc, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Tour provided
tour_check = [0, 5, 10, 4, 11, 0]
total_travel_cost_check = 184.24203302868492

# Validate and print result
result = validate_tour(tour_check, total_travel_cost_check)
print(result)