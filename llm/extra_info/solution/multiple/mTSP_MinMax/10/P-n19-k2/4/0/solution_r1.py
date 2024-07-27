import math
from heapq import heappop, heappush

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute the Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Initialize data structures
num_cities = len(coordinates)
num_robots = 2
tours = {i: [0] for i in range(num_robots)} 
costs = {i: 0 for i in range(num_robots)}

# Priority queue for greedy placement
available_cities = set(range(1, num_cities))
robots_queue = [(0, i) for i in range(num_robots)]

# Greedy algorithm to assign cities to robots aiming for balanced tours
while available_cities:
    current_cost, robot_id = heappop(robots_queue)
    # Find the nearest available city
    last_city = tours[robot_id][-1]
    nearest_city, min_cost = None, float('inf')
    for city in available_cities:
        city_cost = distance(last_city, city)
        if city_cost < min_cost:
            nearest_city, min_cost = city, city_cost
    # Assign the closest city to the robot's tour
    tours[robot_id].append(nearest_city)
    costs[robot_id] += min_cost
    available_cities.remove(nearest_city)
    # Recalculate the priority of the robot
    heappush(robots_queue, (costs[robot_id], robot_id))

# Closing each robot tour back to the depot
for i in range(num_robots):
    last_city = tours[i][-1]
    return_cost = distance(last_city, 0)
    tours[i].append(0)
    costs[i] += return_cost

# Calculate max cost
max_cost = max(costs.values())

# Output required results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")