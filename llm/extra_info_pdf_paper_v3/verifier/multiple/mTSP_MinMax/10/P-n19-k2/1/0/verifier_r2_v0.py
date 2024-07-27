import math

# Input data and solution to be verified
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
robot_0_tour = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 0]
robot_1_tour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0]
robot_0_cost = 263.8480220997549
robot_1_cost = 197.47171059140052

# Expected requirements
total_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_route_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Verification functions
def verify_requirement_1():
    return len(total_cities_visited) == 18 and len(set(total_cities_visited)) == len(total_cities_visited)
    
def verify_requirement_2(tour):
    return tour[0] == 0 and tour[-1] == 0

def verify_requirement_3(robot_costs, expected_max_cost):
    max_cost = max(robot_costs)
    return math.isclose(max_cost, expected_max_cost, rel_tol=1e-9)

def verify_requirement_4():
    computed_robot_0_cost = calculate_total_route_cost(robot_0_tour)
    computed_robot_1_cost = calculate_total_route_cost(robot_1_tour)
    return (math.isclose(computed_robot_0_cost, robot_0_cost, rel_tol=1e-9) 
            and math.isclose(computed_robot_1_cost, robot_1_cost, rel_tol=1e-9))

# Execute verifications
requirement_1 = verify_requirement_1()
requirement_2 = verify_requirement_2(robot_0_tour) and verify_requirement_2(robot_1_tour)
requirement_3 = verify_requirement_3([robot_0_cost, robot_1_cost], max(robot_0_cost, robot_1_cost))
requirement_4 = verify_requirement_4()

# Final result based on requirements
result = "CORRECT" if all([requirement_1, requirement_2, requirement_3, requirement_4]) else "FAIL"
print(result)