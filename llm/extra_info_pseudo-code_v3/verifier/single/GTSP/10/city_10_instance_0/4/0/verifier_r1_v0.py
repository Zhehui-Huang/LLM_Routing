import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tour_length(cities, tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def verify_solution():
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

    groups = [
        {1, 2, 6},
        {3, 7, 8},
        {4, 5, 9}
    ]

    proposed_solution = [0, 6, 7, 5, 0]
    proposed_cost = 74.94753083872993

    # Check starting and ending at depot
    if proposed_solution[0] != 0 or proposed_solution[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group
    visited_groups = [set() for _ in groups]
    for city in proposed_solution[1:-1]:  # exclude the depot at start and end
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i].add(city)
    
    if any(len(g) != 1 for g in visited_groups):
        return "FAIL"
    
    # Check if the tour cost is exactly as provided
    calculated_tour_cost = tour_length(cities, proposed_solution)
    if not math.isclose(calculated_tour_cost, proposed_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Run the test
output = verify_solution()
print(output)