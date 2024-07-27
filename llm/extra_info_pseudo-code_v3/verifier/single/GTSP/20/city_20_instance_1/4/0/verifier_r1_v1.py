import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_cost(tour, expected_cost):
    # Define cities coordinates (index corresponds to city number)
    cities = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91),
        4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
        8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23),
        16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    group_cities = {
        0: [5, 6, 7, 11, 17], 1: [1, 4, 8, 13, 16],
        2: [2, 10, 15, 18, 19], 3: [3, 9, 12, 14]
    }
    found_groups = {}
    for city in tour[1:-1]:
        for group_index, group in group_cities.items():
            if city in group:
                if group_index in found_groups:
                    return "FAIL"
                found_groups[group_index] = True
    if len(found_groups) != 4:
        return "FAIL"

    # [Requirement 3 & 5]
    calc_cost = 0
    for i in range(len(tour)-1):
        calc_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    calc_cost = round(calc_cost, 2)

    if calc_cost != expected_cost:
        return f"FAIL: Calculated cost: {calc_cost} does not match expected cost: {expected_cost}"

    return "CORRECT"

# Given tour and total travel cost
given_tour = [0, 6, 2, 13, 9, 0]
given_total_cost = 108.66

# Execute the test
result = verify_tour_and_cost(given_tour, given_total_cost)
print(result)