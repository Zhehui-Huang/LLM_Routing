import math

# Define city coordinates
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

# Define city groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Proposed solution
tour = [0, 12, 10, 4, 3, 2, 0]
proposed_cost = 138.15

# Calculate the actual distance of the tour
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tour(tour, groups, proposed_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Start or end city is not the depot."
    
    # Check for exactly one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot from this check
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.append(i)
    
    if len(set(visited_group for visited_group in visited_AREA)) != len(set(np.arange(len(color_dict)))):
        return "FAIL", "Does not visit exactly one city from each group."
    
    # Calculating actual travel cost
    actual_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Allow some minor rounding error in floating point calculation
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL", f"Invalid cost calculation. Calculated: {actual_cost}, Expected: {proposed_cost}"
    
    return "CORRECT", ""

# Run verification
result, message = verify_told(tour, color_dict, est_total_cost)
print(result)
if result == "FAIL":
    print(message)