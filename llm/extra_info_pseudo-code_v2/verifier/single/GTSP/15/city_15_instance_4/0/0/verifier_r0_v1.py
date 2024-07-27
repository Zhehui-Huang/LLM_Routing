import math

# Coordinates of each city by index
city_coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# City groups
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Proposed tour and cost
proposed_tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
proposed_cost = 156.56

def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, groups, real_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check unique visit from each group
    visited_from_groups = set()
    for city in tour:
        for idx, group in enumerate(groups):
            if city in group:
                if idx in visited_from_groups:
                    return False
                visited_from_segments.add(idx)
    
    if len(visited_from_groups) != len(groups):
        return False
    
    # Check if computed cost matches the proposed cost accurately
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(tour[i], tour[i+1])
    
    if not math.isclose(computed_cost, real_cost, rel_tol=1e-2):
        return False
    
    return True

# Run the verification
if verify_tour(proposed_tour, city_groups, proposed_cost):
    print("CORRECT")
else:
    print("FAIL")