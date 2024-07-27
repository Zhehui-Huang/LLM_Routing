import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def check_solution():
    # City coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }

    # Proposed solution tour and cost
    tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
    reported_total_cost = 271.47

    if len(tour) != len(set(tour)) + 1:  # Check for depot city being visited twice and others once
        return "FAIL"

    if tour[0] != 0 or tour[-1] != 0:  # Tour must start and end at depot city
        return "FAIL"

    # Calculate the total cost
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        actual_total_cost += compute_euclidean_distance(*cities[city1], *cities[city2])

    # Check if computed cost is approximately equal to the reported cost (allowing for slight numeric discrepancies)
    if not math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-3):
        return "FAIL"

    # If all checks passed, return "CORRECT"
    return "CORRECT"

# Call the function and print the result
print(check_solution())