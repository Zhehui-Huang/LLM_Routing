import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost_claimed):
    # City coordinates
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    # Grouping of cities
    groups = {
        0: [1, 3, 5, 11, 13, 14, 19],
        1: [2, 6, 7, 8, 12, 15],
        2: [4, 9, 10, 16, 17, 18]
    }

    # Check starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check one city from each group
    group_membership = [False] * 3
    for index, city in enumerate(tour[1:-1]):  # Avoid first and last as it's depot
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_membership[group_id]:
                    return "FAIL"  # City from same group already visited
                group_membership[group_id] = True
                break

    if not all(group_membership):
        return "FAIL"

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the calculated cost matches the claimed cost
    if not math.isclose(total_cost, cost_claimed, rel_tol=1e-2):
        return "FAIL"

    # The format of the output appears valid by problem statement, as checked in previous steps.
    return "CORRECT"

# The provided solution
tour_provided = [0, 1, 8, 4, 0]
cost_provided = 110.09

# Execute the test
print(verify_solution(tour_provided, cost_provided))