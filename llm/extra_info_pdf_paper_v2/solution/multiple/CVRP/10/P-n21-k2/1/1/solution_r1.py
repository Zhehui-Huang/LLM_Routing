from itertools import combinations
import math

# Input data setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8,
    11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15
}
robot_capacity = 160
num_robots = 2

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize savings list
savings_list = []
for i, j in combinations(range(1, 21), 2):
    saving = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
    savings_list.append((saving, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])

# Initialize routes
routes = [[i] for i in range(1, 21)]

# Merge routes based on savings, observing capacity constraints
for _, i, j in savings_list:
    for a in range(len(routes)):
        if i in routes[a]:
            index_i = a
        if j in routes[a]:
            index_j = a
    
    if index_i != index_j:
        if sum(demands[k] for k in routes[index_i] + routes[index_j]) <= robot_capacity:
            routes[index_i] += routes[index_j]
            routes[index_j] = []

routes = [r for r in routes if r != []]

# Assign routes to robots
robot_routes = []
for i in range(num_robots):
    robot_routes.append([])

for route in routes:
    robot_routes.sort(key=lambda x: sum(demands[i] for i in x))  # Balance loads
    robot_routes[0].extend(route)

# Calculate the tour details for each robot
total_cost = 0
output = []
for robot_id, tour in enumerate(robot_routes):
    full_tour = [0] + tour + [0]
    cost = sum(euclidean_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour)-1))
    total_cost += cost
    output.append(f"Robot {robot_id} Tour: {full_tour}")
    output.append(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

output.append(f"Overall Total Travel Cost: {total_cost:.2f}")

# Print outputs
for line in output:
    print(line)