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

# Utility functions
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Setup initial routes
routes = {r: [] for r in range(robots)}
current_load = {r: 0 for r in range(robots)}
not_visited = set(cities.keys()) - {0}  # Exclude the depot city

# Assign high demand cities individually if possible
for city in sorted(not_visited, key=lambda x: demands[x], reverse=True):
    if demands[city] > capacity // 2:
        for robot in range(robots):
            if not routes[robot]:  # First try to fill empty route
                routes[robot].append(0)  # Start from the depot
                routes[robot].append(city)
                routes[robot].append(0)  # Return to the depot
                current_load[robot] += demands[city]
                not_visited.remove(city)
                break

# Greedily assign remaining cities
while not_visited:
    made_assignment = False
    for city in sorted(not_visited, key=lambda x: demands[x], reverse=True):
        for robot in range(robots):
            # Check if city can be added without exceeding capacity
            if current_load[robot] + demands[city] <= capacity:
                if city not in routes[robot]:  # Avoid adding a city twice
                    if 0 not in routes[robot]:  # Start with depot if not added
                        routes[robot].insert(0, 0)
                    # Insert before the last element (depot)
                    routes[robot].insert(-1, city)
                    current_load[robot] += demands[city]
                    not_visited.remove(city)
                    made_assignment = True
                    break
        if not made_assignment:
            print(f"Cannot assign city {city} due to capacity constraints.")
            break

# Compute costs
total_cost = 0
for robot, route in routes.items():
    cost = sum(euclidean_dist(route[i], route[i + 1]) for i in range(len(route) - 1))
    total_cost += cost
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")