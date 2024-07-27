import math
from itertools import permutations

# City coordinates and demands
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 
    21: (32, 39), 22: (56, 37)
}
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot capacities and initialization 
robots = 8
capacity = 40

# Util functions
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create initial empty routes
routes = {r: [0] for r in range(robots)}
current_load = {r: 0 for r in range(robots)}
not_visited = set(cities.keys()) - {0} # exclude the depot

# Assignment of cities to routes
while not_visited:
    made_assignment = False
    for city in list(not_visited):  # we use list to snapshot before modification
        for robot in range(robots):
            if current_load[robot] + demands[city] <= capacity:
                # check if adding this city is viable, no hard packing constraints for this example
                routes[robot].append(city)
                current_load[robot] += demands[city]
                not_visited.remove(city)
                made_assignment = True
                break
        if not made_assignment:
            print(f"Cannot assign city {city} due to capacity constraints!")
            break

# Close each robot's tour by returning to the depot
for robot in range(robots):
    routes[robot].append(0)  # return to depot

# Calculate the total travel cost per robot and overall
robot_costs = {}
total_cost = 0

for robot in range(robots):
    route = routes[robot]
    cost = sum(euclidean_dist(route[i], route[i + 1]) for i in range(len(route) - 1))
    robot_costs[robot] = cost
    total_cost += cost
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")