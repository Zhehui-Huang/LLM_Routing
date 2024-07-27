import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
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
    
    # Verify start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify it is a valid tour and visits one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the start and end depot city
        added = False
        for i, group in enumerate(groups):
            if city in group and i not in visited_groups:
                visited_groups.append(i)
                added = True
                break
        if not added:
            return "FAIL"
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate and verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
provided_tour = [0, 8, 4, 2, 5, 1, 7, 0]
provided_total_cost = 257.44

result = verify_solution(provided_tour, provided_total_cost)
print(result)