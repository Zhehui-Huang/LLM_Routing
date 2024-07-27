import math

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c1[0])**2 + (c2[1] - c1[1])**2)

def verify_solution(tour, total_cost):
    # Cities and their coordinates
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # City groups
    groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
                break
    if not all(visited_groups):
        return "FAIL"
    
    # Compute the travel cost and check against provided total cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Tour from the solution
tour = [0, 8, 3, 5, 2, 4, 7, 0]
total_cost = 263.91581915831955

# Verify solution
result = verify_solution(tour, total_cost)
print(result)