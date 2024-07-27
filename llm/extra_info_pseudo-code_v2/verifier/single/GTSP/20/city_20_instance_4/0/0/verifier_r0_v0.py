import math

# Define the coordinates of each city
city_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 
    11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities from which exactly one must be visited
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Proposed solution with the tour and total cost
proposed_tour = [0, 6, 8, 13, 1, 14, 17, 15, 0]
reported_cost = 285.35

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 +
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

def verify_tour(tour, city_groups):
    visited_groups = set()
    
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly one city from each group is visited
    group_visits = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the start and end depot occurrences
        for group_index, group in enumerate(city_groups):
            if city in group:
                group_visits[group_index] += 1
                visited_groups.add(group_index)
                break
    
    if any(v != 1 for v in group_visits) or len(visited_groups) != len(city_groups):
        return False
    
    # Check if overall cost matches the reported cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    # Allow a small floating point margin of error
    if not math.isclose(total_calculated_cost, reported_cost, abs_tol=0.01):
        return False
    
    return True

# Run the verification
if verify_tour(proposed_tour, city_groups):
    print("CORRECT")
else:
    print("FAIL")