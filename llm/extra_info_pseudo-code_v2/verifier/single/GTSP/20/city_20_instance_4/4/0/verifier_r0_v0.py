import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify only one city from each group is visited
    visited_groups = []
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.append(group_index)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Verify the number of cities and coordinates match
    if len(city_coordinates) != 20:
        return "FAIL"
    
    # Verify that the depot city is correctly placed
    if city_coordinates[0] != (26, 60):
        return "FAIL"
    
    # Calculate the total cost from the provided tour and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define cities and coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14],
    [10, 17], [7, 15]
]

# Provided solution
tour_solution = [0, 5, 18, 13, 1, 14, 10, 15, 0]
total_cost_solution = 266.72

# Evaluate the solution
result = verify_solution(tour_solution, total_cost_solution, cities, groups)
print(result)