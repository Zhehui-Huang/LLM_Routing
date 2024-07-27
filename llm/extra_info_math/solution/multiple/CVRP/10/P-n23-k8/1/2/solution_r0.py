import math
from itertools import combinations

# Coordinates and demands
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
          (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacity = 40
num_robots = 8

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Compute distances matrix
n = len(coords)
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings Algorithm
def savings_algorithm():
    savings = [(i, j, distances[0][i] + distances[0][j] - distances[i][j])
               for i in range(1, n) for j in range(i + 1, n)]
    savings.sort(key=lambda x: x[2], reverse=True)
    routes = [[0, i, 0] for i in range(1, n)]
    unmerged = set(range(1, n))

    while len(savings) > 0:
        i, j, saving = savings.pop(0)
        if i in unmerged and j in unmerged:
            routes.append([0, i, j, 0])
            unmerged.remove(i)
            unmerged.remove(j)

    return routes

# Create initial routes based on savings
initial_routes = savings_algorithm()

# Assign routes to vehicles considering capacity constraints
def assign_routes_to_robots(routes):
    robot_tours = [[] for _ in range(num_robots)]
    demands_met = [0] * len(demands)
    routes_used = []

    for route in routes:
        if sum(demands[city] for city in route if city != 0) <= capacity:
            found_robot = False
            for robot_id in range(num_robots):
                if sum(demands_met[city] for city in robot_tours[robot_id]) + sum(demands[city] for city in route) <= capacity:
                    demands_met = [demands_met[i] + (demands[i] if i in route else 0) for i in range(len(demands))]
                    robot_tours[robot_id].extend(route)
                    routes_used.append(route)
                    found_robot = True
                    break
            if not found_robot:
                return [], False  # No feasible allocation found
    return robot_tours, True

robot_tours, feasible = assign_routes_to_robots(initial_routes)

# Calculate traveled distance and output the results
total_distance = 0
if feasible:
    for robot_id, tour in enumerate(robot_tours):
        tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}\n")
        total_distance += tour_cost
    print(f"Overall Total Travel Cost: {total_distance}")
else:
    print("A feasible solution could not be found with the given number of robots and their capacities.")