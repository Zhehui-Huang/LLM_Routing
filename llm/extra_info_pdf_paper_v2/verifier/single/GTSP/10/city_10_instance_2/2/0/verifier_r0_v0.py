import math

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_tour(tour, city_positions, city_groups):
    # Requirement 1: The robot must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 4: The robot needs to visit exactly one city from each group.
    visited_groups = set()
    for city in tour[1:-1]:  # ignore the depot city at the start/end
        for group_id, group in enumerate(city_groups):
            if city in group:
                if group_id in visited_groups:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups.add(group_id)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Not all groups were visited
    
    # Requirement 2 & 3: Travelling between any two cities and calculate travel cost
    total_calculated_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i+1]
        total_calculated_distance += calculate_euclidean_distance(city_positions[city_a], city_positions[city_b])
    
    # Using the provided total travel cost (as verification isn't feasible without the correct expected cost)
    known_travel_cost = 281.6
    if not math.isclose(total_calculated_distance, known_travel_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Test data (as per task description)
city_positions = {
    0: (90, 3), 
    1: (11, 17), 
    2: (7, 27), 
    3: (95, 81), 
    4: (41, 54), 
    5: (31, 35), 
    6: (23, 95), 
    7: (20, 56), 
    8: (49, 29), 
    9: (13, 17)
}
city_groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

test_tour = [0, 3, 5, 9, 1, 2, 0]

# Running verification
result = verify_tour(test_tour, city_positions, city_groups)
print(result)