import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, groups, expected_cost):
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is included
    group_check = set()
    for city in tour[1:-1]:  # skipping the depot city in start and end
        found_group = False
        for idx, group in enumerate(groups):
            if city in group:
                if idx in group_check:
                    return "FAIL"  # City from the same group has already been included
                group_check.add(idx)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if len(group_check) != len(groups):
        return "FAIL"
    
    # Calculate the actual travel cost and compare with the given
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(actual_cost, expected_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"


# Given cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13],
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Tour provided and the given total cost
provided_tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
provided_cost = 266.72

# Validate the tour
result = verify_tour(provided_tour, cities, groups, provided_cost)
print(result)