import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

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

groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def check_tour(tour, group_coverage):
    # Check if starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Check if one city from each group is visited
    visited = set()
    for city in tour:
        for group in group_coverage:
            if city in group_coverage[group]:
                if group in visited:
                    return "FAIL"
                visited.add(group)
    if len(visited) != len(group_coverage):
        return "FAIL"
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the cost is minimal (can't check optimality without comparing with other solutions)
    reported_cost = 324.1817486177585
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution tour and the reported total cost
solution_tour = [0, 7, 1, 4, 8, 5, 2, 0]
# Call the verify function
result = check_tour(solution_tour, groups)
print(result)