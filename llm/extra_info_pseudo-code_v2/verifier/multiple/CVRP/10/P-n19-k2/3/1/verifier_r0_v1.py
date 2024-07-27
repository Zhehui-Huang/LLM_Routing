import math

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
               (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot tours and details
robots = {
    0: [0, 16, 0, 8, 0, 3, 0, 17, 0, 13, 0, 9, 0, 12, 0, 14, 0, 11, 0, 5, 0, 7, 0], 
    1: [0, 3, 0, 8, 0, 12, 0, 9, 0, 16, 0, 17, 0, 14, 0, 13, 0, 5, 0, 4, 0]
}
robot_capacity = 160

# Calculate the Euclidean distance between two points
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Validate the solution
def validate_solution(robots, demands, robot_capacity):
    city_demand_satisfied = [0] * len(demands)
    
    for tours in robots.values():
        for i in range(len(tours) - 1):
            if tours[i] != 0:
                city_demand_satisfied[tours[i]] += demands[tours[i]]
                
    if not all(c == demands[i] for i, c in enumerate(city_demand_satisfied) if i != 0):
        return "FAIL: Demand not met for all cities"

    # Check start and end at the depot
    for tour in robots.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"

    # Validate each robot does not exceed its capacity
    for robot_id, tour in robots.items():
        load = 0
        for i in range(len(tour) - 1):
            if tour[i+1] != 0:
                load += demands[tour[i+1]]
                if load > robot_capacity:
                    return f"FAIL: Robot {robot_id} exceeds capacity"
            if tour[i+1] == 0:
                load = 0  # reset load at depot

    return "CORRECT"

# Run validation
result = validate_solution(robots, demands, robot_capacity)
print(result)