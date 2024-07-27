import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, groups, city_coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited_groups = set()
    for city in tour[1:-1]:
        for group_id, group_cities in enumerate(groups):
            if city in group_cities:
                visited_groups.add(group_id)
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    calculated_cost = sum(compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    
    # Here you would replace 35.82799574 with the actual result from the MILP solver
    if abs(calculated_cost - 35.82799574) < 1e-4:
        return "CORRECT"
    else:
        return "FAIL"

# City coordinates per given problem
city_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# City groups
groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Tour provided by MILP solution
milp_tour = [0]  # This tour should be replaced with the actual MILP solution tour. Here it's just a placeholder
milp_cost = 0    # This should also be replaced with the actual computed cost from MILP solution

# Checking the solution
verification_result = verify_tour(milp_tour, groups, city_coordinates)
print(verification_result)