import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Verify Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: One city per group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot at start and end
        for idx, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(idx)
                break
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Verify Requirement 3 and Requirement 4: Correct distances and tour total
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by the city index
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups indexed by their group number
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Solution details
tour = [0, 16, 18, 13, 3, 2, 10, 7, 0]
total_cost = 497.18

# Verify the solution
result = verify_solution(tour, total_cost, city_coordinates, city_groups)
print(result)