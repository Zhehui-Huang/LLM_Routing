import math

# Given problem data
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160

# Solution
robot_0_tour = [0, 1, 2, 3, 4, 5, 6, 7, 9, 0]
robot_1_tour = [0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tours():
    # Check if tours start and end with depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL"
    if robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"
    
    # Check if every city is visited once and demands are met
    supplied = [0] * len(demands)
    for i, tour in enumerate([robot_0_tour, robot_1_tour]):
        current_capacity = robot_capacity
        for j in range(1, len(tour) - 1):  # exclude depot
            city = tour[j]
            demand = demands[city]
            if current_capacity < demand:
                return "FAIL"
            current_capacity -= demand
            supplied[city] += demand
    
    if any(supplied[city] != demands[city] for city in range(1, len(demands))):
        return "FAIL"
    
    # Verify total capacity not exceeded
    for tour in [robot_0_tour, robot_1_tour]:
        total_demand = sum(demands[city] for city in tour if city != 0)
        if total_demand > robot_capacity:
            return "FAIL"
    
    # Calculate travel cost and verify (need correct solutions provided)
    robot_0_cost = sum(calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
                       for i in range(len(robot_0_tour) - 1))
    robot_1_cost = sum(calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
                       for i in range(len(robot_1_tour) - 1))
    overall_cost = robot_0_cost + robot_1_cost
    expected_total_cost = 171.92 + 305.44

    if not math.isclose(overall_cost, expected_total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Running the verification
print(verify_tours())