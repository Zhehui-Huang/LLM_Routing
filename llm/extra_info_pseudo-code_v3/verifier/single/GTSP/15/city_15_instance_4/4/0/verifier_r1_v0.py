import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Test configuration
city_positions = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]
expected_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
expected_cost = 220.73

def check_tour_starts_and_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def check_one_city_per_group(tour, groups):
    visited = set(tour[1:-1])  # Exclude the depot city from both ends
    return all(len(visited.intersection(group)) == 1 for group in groups)

def check_total_travel_cost(tour, positions):
    total_cost = sum(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, expected_cost, rel_tol=1e-2)

def verify_solution():
    if not check_tour_starts_and_ends_at_depot(expected_tour):
        return "FAIL"
    if not check_one_city_per_group(expected_tour, city_groups):
        return "FAIL"
    if not check_total_travel_cost(expected_tour, city_positions):
        return "FAIL"
    return "CORRECT"

# Execute the test and print the result
print(verify_solution())