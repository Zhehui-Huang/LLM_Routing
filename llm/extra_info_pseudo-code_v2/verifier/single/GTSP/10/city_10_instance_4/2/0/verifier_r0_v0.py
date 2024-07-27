import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution():
    # City coordinates
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80),
        3: (65, 26), 4: (92, 9), 5: (83, 61),
        6: (22, 21), 7: (97, 70), 8: (20, 99),
        9: (66, 62)
    }
    
    # City groups
    city_groups = {
        0: [1, 4], 1: [2, 6], 2: [7], 3: [5],
        4: [9], 5: [8], 6: [3]
    }
    
    # Provided solution
    tour = [0, 3, 6, 8, 9, 5, 7, 4, 0]
    reported_cost = 307.34884024239136

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check calculated cost against reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group NOid)

    # Ensure all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    return "CORRECT"

# Run the test and print result
print(test_solution())