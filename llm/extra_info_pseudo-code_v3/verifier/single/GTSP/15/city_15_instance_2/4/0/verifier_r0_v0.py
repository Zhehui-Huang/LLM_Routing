import math

# Given city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Groups of cities
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Provided solution details
proposed_tour = [0, 12, 10, 4, 3, 2, 0]
proposed_cost = 138.15

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, proposed_cost):
    # Check Requirement 1: Starts and ends at depot (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Exactly one city from each group
    visited = set(tour[1:-1])  # exclude the depot city at start and end
    for group in city_groups:
        if len(set(group).intersection(visited)) != 1:
            return "FAIL"
    
    # Check Requirement 4: The tour starts and ends at the depot city
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check accumulated travel distance
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    # Check Requirement 5: Output the total travel cost of the tour
    # Allow a small rounding error in floating point calculations
    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the verification and print the result
result = verify_tour(proposed_tour, proposed_cost)
print(result)