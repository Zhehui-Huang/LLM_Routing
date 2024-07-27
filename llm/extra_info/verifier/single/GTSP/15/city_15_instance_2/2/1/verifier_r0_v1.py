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
provised_cost = 138.15

# Calculate the actual distance of the tour
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tour(tour, groups, proposed_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city."
    
    # Check for exactly one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot from this check
        found_group = False
        for idx, group in enumerate(groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL", "A group is visited more than once."
                visited_groups.append(idx)
                found_group = True
                break
        if not found_group:
            return "FAIL", "A city outside the defined groups was visited."

    if len(set(visited_groups)) != len(groups):
        return "FAIL", f"Not all groups are visited. Visited groups: {visited_groups}"

    # Calculating actual travel cost
    actual_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Allow some minor rounding error in floating point calculations
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL", f"Travel cost mismatch. Calculated: {actual_cst}, Expected: {proposed_cost}"
    
    return "CORRECT", ""

# Run verification
result, message = verify_tour(tour, e_groups, cutoff_lat_cost)
print(result)
if result == "FAIL":
    print(message)