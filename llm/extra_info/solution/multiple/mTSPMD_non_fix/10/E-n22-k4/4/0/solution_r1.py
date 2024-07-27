import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots (currently all starting from position 0 due to no differentiation mentioned)
num_robots = 4
depots = [0 for _ in range(num_robots)]  # Each robot starts at depot(city index 0)

# Calculate Euclidean distance between two points
def calculate_distance(index1, index2):
    return euclidean(cities[index1], cities[index2])

# Provides an initial route based on the nearest unvisited neighbor heuristic
def initial_route(start_index, unvisited):
    route = [start_index]
    current = start_index
    while unvisited:
        nearest = min(unvisited, key=lambda x: calculate_distance(current, x))
        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    return route

# Two-opt optimization
def two_opt(route):
    min_change = True
    while min_change:
        min_change = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum([calculate_distance(new_route[k], new_route[k-1]) for k in range(1, len(new_route))]) < \
                   sum([calculate_distance(route[k], route[k-1]) for k in range(1, len(route))]):
                    route = new_route
                    min_change = True
    return route

# Assign cities to clusters
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(cities))
labels = kmeans.labels_

# Assigning initial routes for robots based on clustering
robot_routes = {i: initial_route(depots[i], [index for index, label in enumerate(labels) if label == i]) for i in range(num_robots)}

# Optimizing each robot's route individually using 2-opt
optimized_routes = {}
total_cost = 0

for r in robot_routes:
    optim_route = two_opt(robot_routes[r])
    route_cost = sum([calculate_distance(optim_route[i], optim_route[i-1]) for i in range(1, len(optim_route))])
    optimized_routes[r] = (optim_route, route_cost)
    total_cost += route_cost

# Output results
for robot, (route, cost) in optimized_routes.items():
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel_FUNCost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")