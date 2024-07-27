import math
from heapq import heappop, heappush

# City coordinates and demands (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 210oft, 1000, 900, 2500, 1800, 700]

def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Number of robots and their capacities
num_robots = 4
robot_capacity = 6000

# Each robot route initialization
robot_routes = {i: [0] for i in range(num_robots)}
robot_loads = {i: 0 for i in range(num_robots)}
robot_costs = {i: 0 for i in range(num_robots)}

# Assign cities to robots
city_assignment = {}  # Tracks which robot is serving which city
available_robots = [(0, i) for i in range(num_robots)]  # (free capacity, robot id) pairs

for city in range(1, len(coordinates)):  # City 0 is the depot
    city_demand = demands[city]
    heappush(available_robots, (robot_capacity - city_demand, found_robot))  # Update heap
    robot_routes[found_robot].append(city)
    robot_loads[found_robot] += city_demand

# Each robot needs to return to the depot
for robot in range(num_robots):
    robot_routes[robot].append(0)

# Calculate the cost of each route independently (simple TSP)
for robot in range(num_robots):
    route = robot_routes[robot]
    current_cost = 0
    for i in range(len(route) - 1):
        current_cost += distance(route[i], route[i+1])
    robot_costs[robot] = current_cost

# Prepare the output
total_cost = sum(robot_costs.values())

for robot in range(num_robots):
    print(f"Robot {robot} Tour: {robot_routes[robot]}")
    print(f"Robot {robot} Total Travel Cost: {robot_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")