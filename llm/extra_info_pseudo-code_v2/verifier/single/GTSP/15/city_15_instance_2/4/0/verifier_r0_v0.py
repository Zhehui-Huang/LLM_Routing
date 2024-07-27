import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_cost):
    # Define city coordinates
    cities = [
        (54, 87),  # Depot city 0
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99)    # City 14
    ]

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    visited_groups = set()
    for index in tour:
        for i, group in enumerate(groups):
            if index in group:
                visited_groups.add(i)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate the travel cost and compare with provided total cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 8, 11, 6, 2, 0]
total_cost = 103.11611697272403

# Check if the solution passes all tests
result = check_solution(tour, total_cost)
print(result)