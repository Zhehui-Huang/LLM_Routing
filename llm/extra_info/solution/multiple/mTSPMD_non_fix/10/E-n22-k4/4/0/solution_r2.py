import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots and their starting depots
num_robots = 4
depots = [0] * num_robots  # all robots start from city 0 as per scenario

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Optimize route using a simple 2-opt algorithm adapted for lists of city indices
def two_opt(route):
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_route) - 1):
            for j in range(i+1, len(best_route)):
                if j-i == 1: continue
                new_route = best_route[:i] + best_route[i:j][::-1] + best_route[j:]
                if sum(calculate_distance(new_route[k], new_route[k-1]) for k in range(1, len(new_route))) < \
                   sum(calculate[length(best_route[k], best_route[k-1]) for k in range(1, len(best_route))]):
                    best_route = new_route
                    improved = True
    return best_route

# Using KMeans to cluster cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots)
assignment = kmeans.fit_predict(np.array([cities[c] for c in cities]))

# Creating initial routes for each robot and optimizing them
routes = {r: [depots[r]] for r in range(num_robots)}
for city_index, assigned_robot in enumerate(assignment):
    if city_index != depots[0]:  # Exclude the depot from re-assignment
        routes[assigned_robot].append(city_index + 1)  # Compensate for zero-indexed depot

optimized_routes = {}
total_travel_cost = 0

for robot_id, route in routes.items():
    # Ensure starting at depot and performing tour optimization
    optimized_route = two_opt(route)
    route_cost = sum(calculate_distance(optimized_route[i], optimized_route[i-1]) for i in range(1, len(optimized_route)))
    optimized_routes[robot_id] = (optimized_route, route_cost)
    total_travel_cost += route_cost

# Output the optimized routes and costs
for robot_id, (route, cost) in optimized_routes.items():
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travelixe_cost}")