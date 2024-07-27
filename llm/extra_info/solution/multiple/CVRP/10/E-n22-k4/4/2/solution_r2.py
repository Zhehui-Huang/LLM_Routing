import math

# City coordinates and demands (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Number of robots and their capacities
num_robots = 4
robot_capacity = 6000

# Routes and loads for robots, initialized
robot_routes = {i: [0] for i in range(num_robots)}
robot_loads = {i: 0 for i in range(num_robots)}
robot_costs = {i: 0 for i in range(num_robots)}

# Sort cities by demand in descending order for easier load balancing
sorted_cities = sorted(list(range(1, len(coordinates))), key=lambda x: demands[x], reverse=True)

# Assign cities to robots balancing the load
for city in sorted_cities:
    # Find the robot with the lowest load to which we can still assign this city
    min_load_robot = min((robot for robot in range(num_robots) if robot_loads[robot] + demands[city] <= robot_capacity),
                         key=lambda r: robot_loads[r], default=None)
    if min_load_robot is not None:
        robot_routes[min_load_robot].append(city)
        robot_loads[min_load_robot] += demands[city]
    else:
        print("It's not possible to distribute cities among the robots without exceeding capacity. Please check configurations.")
        break

# Finish routes with a return to the depot
for robot in range(num_robots):
    robot_routes[robot].append(0)

# Calculate the travel costs
total_cost = 0

for robot in range(num_robots):
    route_cost = 0
    route = robot_routes[robot]
    for i in range(len(route) - 1):
        route_cost += distance(route[i], route[i + 1])
    robot_costs[robot] = route_cost
    total_cost += route_cost

# Print results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {robot_routes[robot]}")
    print(f"Robot {robot} Total Travel Cost: {robot_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")