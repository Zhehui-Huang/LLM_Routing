import math

# Define cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Define city groups
city_groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

# Given solution tour and total cost
given_tour = [0, 6, 8, 13, 9, 4, 17, 15, 0]
given_cost = 363.34

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_tour_requirements(tour, expected_cost):
    # Requirement 1: Start and End at City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: One city from each group
    visited_groups = [set() for _ in range(len(city_groups))]
    for i in range(len(tour)):
        for group_id, members in city_groups.items():
            if tour[i] in members:
                visited_groups[group_id].add(tour[i])
    if any(len(group) != 1 for group in visited_groups):
        return "FAIL"
    
    # Calculate actual cost
    actual_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # Requirement 3: Minimized total cost (assumed based on given data, check if provided)
    # We tolerate a little floating point precision error.
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Check if the provided solution meets the requirements
test_result = verify_tour_requirements(given_tour, given_cost)
print(test_result)