import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
city_groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

# Test tour and reported total travel cost
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
reported_cost = 266.71610174713

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_tour(tour):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot"
    
    # Check one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the depot city in the checks
        found_group = False
        for group, members in city_groups.items():
            if city in members:
                if group in visited_groups:
                    return "FAIL: More than one city from a single group visited"
                visited_groups.add(group)
                found_group = True
                break
        if not found_group:
            return "FAIL: City does not belong to any group"
    
    if len(visited_groups) != len(city_groups):
        return "FAIL: Not all groups are represented"
    
    # Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost {calculated_cost} does not match reported cost {reported_cost}"
    
    return "CORRECT"

# Run the test
result = test_tour(tour)
print(result)