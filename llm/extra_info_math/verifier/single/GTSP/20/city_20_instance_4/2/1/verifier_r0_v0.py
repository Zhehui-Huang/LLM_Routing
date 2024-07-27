import math

# City coordinates including depot city at index 0
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Group of cities by group index
city_groups = {
    0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 3: [1, 3, 9], 
    4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
}

# Proposed solution
proposed_tour = [0]
proposed_cost = 0  # Provided as 0 incorrectly, need to compute and validate


def compute_euclidean_distance(city1, city2):
    """ Compute Euclidean distance between two cities based on their coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def check_tour(tour, cost):
    # Check if tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    visited_groups = {}
    for city in tour:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups[group_id] = 1
    
    # All groups must be visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Verify the reported cost by calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += compute_euclidean_distance(tour[i], tour[i + 1])

    # Due to rounding and truncation in some solvers, we compare with a small tolerance
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"


# Check the proposed solution
result = check_tour(proposed_tour, proposed_cost)
print(result)