import math

def euclidean_distance(p1, p2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tsp_solution(tour, total_cost, city_coordinates, groups):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = {i: False for i in range(len(groups))}
    for city_index in tour[1:-1]:  # Exclude the depot city at start/end
        for group_index, cities in enumerate(groups):
            if city_index in cities:
                if visited_groups[group_index]:
                    return "FAIL"
                visited_groups[group\"_index] = True
                break
    if not all(visited_groups.values()):
        return "FAIL"

    # Calculate the total travel cost from the tour and compare with given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Allow for a small numerical error margin
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
city_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities
groups = [
    [8, 12, 14],  # Group 0
    [7, 10, 11],  # Group 1
    [4, 6, 9],    # Group 2
    [1, 3, 13],   # Group 3
    [2, 5]        # Group 4
]

# Provided solution
tour = [0, 1, 8, 11, 6, 2, 0]
total_cost = 103.12

# Verify the solution
result = verify_tsp_solution(tour, total_cost, city_coordinates, groups)
print(result)