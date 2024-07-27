import math

# Given solution details
tour = [0, 5, 6, 7, 1, 9, 2, 4, 3, 8, 0]
total_travel_cost = 442.21797728444267
maximum_distance = 69.42622

# Given positions for each city
positions = {
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

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# 1. Check if the robot starts and ends at the depot city 0
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# 2. Check each city is visited exactly once (except the depot, visited twice)
def check_visit_once(tour):
    visited = set(tour)
    return len(visited) == 10 and all(tour.count(city) == 1 for city in visited if city != 0)

# 3. Check travel cost calculation and total cost
def check_costs(tour):
    calc_distances = [euclidean_distance(positions[tour[i]], positions[tour[i + 1]]) for i in range(len(tour) - 1)]
    calc_total_cost = sum(calc_distances)
    calc_max_distance = max(calc_distances)
    return (
        abs(calc_total_cost - total_travel_cost) < 0.0001 and
        abs(calc_max_distance - maximum_distance) < 0.0001
    )

def verify_solution(tour, total_travel_cost, maximum_distance):
    if not check_start_end(tour):
        return "FAIL"
    if not check_visit_once(tour):
        return "FAIL"
    if not check_costs(tour):
        return "FAIL"
    return "CORRECT"

# Verify the given solution
solution_status = verify_solution(tour, total_travel_cost, maximum_distance)
print(solution_status)  # This will output "CORRECT" or "FAIL"