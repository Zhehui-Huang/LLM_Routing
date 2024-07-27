import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, expected_cost):
    city_coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }
    
    # Verify start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify visiting exactly one city from each group
    visited_from_group = {0: False, 1: False, 2: False}
    
    for index in tour[1:-1]:  # Ignore the first and last, as these should be the depot
        found = False
        for group, cities in groups.items():
            if index in cities:
                if visited_from_group[group]:
                    return "FAIL"
                visited_from_group[group] = True
                found = True
                break
        if not found:
            return "FAIL"
    
    if not all(visited_from_group.values()):
        return "FAIL"
    
    # Verify travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided sample tour and expected cost
sample_tour = [0, 6, 7, 5, 0]
expected_cost = 74.95

# Verification of the sample tour
result = verify_solution(sample_tour, expected_cost)
print(result)