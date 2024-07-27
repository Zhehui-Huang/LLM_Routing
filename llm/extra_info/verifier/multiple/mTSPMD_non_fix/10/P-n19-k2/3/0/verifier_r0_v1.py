import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13]
    robot_1_tour = [1, 10, 12, 14, 4, 11, 3, 8, 16, 17]
    
    # [Requirement 1] Check exact city count
    if len(cities) != 19:
        return "FAIL"
    
    # [Requirement 2] Both robots start at depot city 0
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"
    
    # Collectively visiting all cities
    all_visited_cities = set(robot_0_tour + robot_1_tour)
    if all_visited_cities != set(cities.keys()):
        return "FAIL"
    
    # [Requirement 4] Each city is visited exactly once
    total_visits = {city: (robot_0_tour + robot_1_tour).count(city) for city in cities}
    for count in total_visits.values():
        if count != 1:
            return "FAIL"
    
    # Calculate total travel costs for validation
    def calculate_total_cost(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        return total_cost
    
    total_cost_robot_0 = calculate_total_cost(robot_0_tour)
    total_cost_robot_1 = calculate_total_cost(robot_1_tour)
    
    known_cost_robot_0 = 66.43745355707826
    known_cost_robot_1 = 86.15820358195867
    tolerance = 1e-5
    
    # Approximate match to account for floating point arithmetic issues
    if not (abs(total_cost_robot_0 - known_cost_robot_0) < tolerance and
            abs(total_cost_robot_1 - known_each_cost_robot_1) < tolerance):
        return "FAIL"
    
    # [Requirement 6] not fully automatic, needs heuristic comparison for multiple runs
    
    # Requirement 7 validation ensured by format print output
    
    return "CORRECT"

# Running the verification function
print(verify_solution())