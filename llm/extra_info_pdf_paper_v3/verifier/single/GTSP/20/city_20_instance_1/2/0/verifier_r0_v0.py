import math

# Define the cities and their groups
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

groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Test tour and cost
proposed_tour = [0, 6, 13, 2, 9, 0]
proposed_cost = 114.65928837582914

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tour(tour, cost):
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Check Requirement 2: One city from each group
    visited_groups = [next(key for key, group in groups.items() if city in group) for city in tour[1:-1]]
    if len(set(visited_groups)) != len(groups):
        return "FAIL"

    # Check Requirement 3: Calculate the total cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[i], tour[i+1])
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = verify_tour(proposed_tour, proposed_cost)
print(result)