import math

# Coordinate and demand definitions
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot parameters
robot_capacity = 160
num_robots = 2

# Helper function to compute distance
def euclidean_distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Assign cities to robots attempting to minimize cost
robots = {i: {'route': [0], 'load': 0, 'cost': 0} for i in range(num_robots)}
available_cities = set(range(1, len(coordinates)))

while available_cities:
    for robot_id, robot in robots.items():
        min_distance = float('inf')
        next_city = None
        for city in available_cities:
            distance = euclidean_distance(robot['route'][-1], city)
            if distance < min_distance and robot['load'] + demands[city] <= robot_capacity:
                min_distance = distance
                next_city = city
        
        if next_city is not None:
            robot['route'].append(next_city)
            robot['load'] += demands[next_city]
            robot['cost'] += min_distance
            available_cities.remove(next_city)

# Finalize routes by returning to the depot
overall_cost = 0
for robot_id, robot in robots.items():
    # Return to depot
    return_cost = euclidean_distance(robot['route'][-1], 0)
    robot['route'].append(0)
    robot['cost'] += return_cost
    overall_cost += robot['cost']
    
    # Output details for each robot
    print(f"Robot {robot_id} Tour: {robot['route']}")
    print(f"Robot {robot_id} Total Travel Cost: {robot['cost']}")

# Overall cost
print(f"Overall Total Travel Cost: {overall_cost}")