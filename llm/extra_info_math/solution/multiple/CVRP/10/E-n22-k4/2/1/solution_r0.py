import math
from collections import defaultdict

# City coordinates and demand data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]
num_robots = 4
robot_capacity = 6000

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calculate distances
N = len(coordinates)
distances = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Clarke and Wright Savings Algorithm
def clarke_and_wright():
    savings = []
    for i in range(1, N):
        for j in range(1, N):
            if i != j:
                savings.append(((i, j), distances[0][i] + distances[0][j] - distances[i][j]))
    savings.sort(key=lambda x: x[1], reverse=True)

    routes = []
    load = {}
    route_of = {}

    for (i, j), _ in savings:
        if i not in route_of and j not in route_of:
            if demands[i] + demands[j] <= robot_capacity:
                # Start a new route
                routes.append([0, i, j, 0])
                load[len(routes)-1] = demands[i] + demands[j]
                route_of[i] = route_of[j] = len(routes)-1
        elif i in route_of and j not in route_of:
            idx = route_of[i]
            if routes[idx][-2] == i and load[idx] + demands[j] <= robot_capacity:
                # Expand route at end
                routes[idx].insert(-1, j)
                load[idx] += demands[j]
                route_of[j] = idx
        elif i not in route_of and j in route_of:
            idx = route_of[j]
            if routes[idx][1] == j and load[idx] + demands[i] <= robot_capacity:
                # Expand route at start
                routes[idx].insert(1, i)
                load[idx] += demands[i]
                route_of[i] = idx

    # All unassigned cities must start a new tour
    for i in range(1, N):
        if i not in route_of:
            if demands[i] <= robot_capacity:
                routes.append([0, i, 0])
                load[len(routes)-1] = demands[i]
                route_of[i] = len(routes) - 1

    return routes, load

routes, load = clarke_and_wright()

# Display the final routes and calculate total cost
total_cost = 0
for r, route in enumerate(routes):
    tour_cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += tour_cost
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")