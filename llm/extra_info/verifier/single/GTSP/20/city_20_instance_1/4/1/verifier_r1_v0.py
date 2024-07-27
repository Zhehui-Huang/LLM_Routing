import math

# Define coordinates for cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Define city groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Tour solution provided
tour_provided = [0, 6, 13, 2, 9, 0]
cost_provided = 114.65928837582914

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to verify the tour
def verify_tour_and_cost(tour, cost):
    visited_groups = set()

    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if it visits exactly one city from each group
    for index, city in enumerate(tour):
        if index == 0 or index == len(tour) - 1:
            continue
        for group_id, group in city_groups.items():
            if city in group:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)

    # Must visit all city groups
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check the calculated travel cost
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(tour[i], tour[i+1])
    
    if not math.isclose(calc_cost, cost, abs_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test the given solution
result = verify_tour_and_cost(tour_provided, cost_provided)
print(result)