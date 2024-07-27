import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(cities, city_groups, tour):
    # Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check one city from each group visited
    visited_groups = set()
    for city_index in tour[1:-1]:  # Omit the depot city at start and end
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(city_groups):
        return False

    # Calculate travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Check the travel cost matches expected
    if not math.isclose(total_cost, 162.38, abs_tol=0.01):
        return False
    
    return True

# Define city coordinates (including the depot)
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Define city groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Tour provided in the solution
proposed_tour = [0, 11, 16, 18, 19, 6, 0]

# Validate the tour
if validate_tour(cities, city_groups, proposed_tour):
    print("CORRECT")
else:
    print("FAIL")