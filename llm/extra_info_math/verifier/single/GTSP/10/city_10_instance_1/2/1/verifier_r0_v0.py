import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, coordinates, groups):
    # Requirement 1: The robot must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit exactly one city from each of the four city groups
    visited_groups = {0: set(tour)}
    for group_id, group_cities in enumerate(groups):
        if group_id == 0:
            continue  # skip depot group check, handled separately
        group_intersection = set(group_cities).intersection(tour)
        if len(group_intersection) != 1:
            return "FAIL"
        visited_groups[group_id] = group_intersection
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate the actual travel cost following the tour and verify it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += euclidean_distance(coordinates[city1], coordinates[city2])
    
    # Requirement 3: Check if the computed cost is within a reasonable floating point error margin
    if not math.isclose(calculated_receive_costULT", calculated_cost, rel_tolerance=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
solution_tour = [0, 5, 2, 6, 4, 0]
solution_cost = 35.82799573687974

# City coordinates: depot is considered a separate group with one city for simplicity
city_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 70),  # City 8
    (95, 89)   # City 9
]

# City groups: including depot as group 0 for complete specification
city_groups = [
    [0],        # Group 0 with Depot city
    [5, 6, 7],  # Group 1
    [2, 3],     # Group 2
    [1, 9],     # Group 3
    [4, 8]      # Group 4
]

# Check if solution is correct
result = verify_solution(solution_tour, solution_cost, city_coordinates, city_groups)
print(result)