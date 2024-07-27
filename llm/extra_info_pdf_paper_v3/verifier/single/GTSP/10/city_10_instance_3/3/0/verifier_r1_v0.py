import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour():
    # City coordinates
    city_coordinates = {
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
    city_groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]
    
    # Provided solution
    proposed_tour = [0, 7, 1, 4, 8, 5, 2, 0]
    proposed_total_cost = 324.18
    
    # Verify start and end at the depot
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Verify each group is represented exactly once
    visited_groups = [False] * len(city_groups)
    for city in proposed_tour:
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
    if not all(visited_groups):
        return "FAIL"
    
    # Calculate the actual travel cost of the proposed tour
    actual_cost = 0
    for i in range(len(proposed_tour) - 1):
        city_a = proposed_tour[i]
        city_b = proposed_tour[i + 1]
        actual_cost += calculate_euclidean_distance(
            city_coordinates[city_a][0], city_coordinates[city_a][1],
            city_coordinates[city_b][0], city_coordinates[city_b][1]
        )
    
    # Compare the calculated cost with the proposed cost
    if not math.isclose(actual_cost, proposed_total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run verification
print(verify_tour())