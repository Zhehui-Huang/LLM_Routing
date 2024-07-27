import math

def euclidean_distance(city_a, city_b):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Check the cities count
    if len(city_coordinates) != 15:
        return "FAIL"

    # Check tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the robot visits exactly one city from each group
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # skip the first and last since those are the depot
        found_group = False
        for i, group in enumerate(city_modes):
            if city in group:
                visited_groups[i] += 1
                found_group = True
                break
        if not found_group:
            return "FAIL"
                
    if any(v != 1 for v in visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Compare the given total cost with the calculated cost
    if math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "CORRECT"
    else:
        return "FAIL"

# Given input setup
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

tour = [0, 13, 14, 8, 10, 12, 2, 5, 0]
total_cost = 211.5

# Execute verification
print(verify_solution(tour, total_cost, city_coordinates, city_groups))