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

# Number of robots and their starting depots:
num_robots = 4
depots = [0, 0, 0, 0]  # all starting from city index 0 as per scenario

def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(calculate_distance(new_route[k], new__route[k-1]) for k in range(1, len(new_route))) < \
                   sum(calculate_distance(best[k], best[k-1]) for k in range(1, len(best))):
                    best = new_route
                    improved = True
        route = best
    return best

# Assign cities to robots using KMeans clustering
city_points = np.array([cities[i] for i in range(len(cities))])
kmeans = KMeans(n_clusters=num_robots, init=np.array([cities[d] for d in depots[:num_robots]]), n_init=1)
assignments = kmeans.fit_predict(city_points)

# Create initial routes for each robot
routes = {i: [depots[i]] for i in range(num_robots)}
for city_index, assigned_robot in enumerate(assignments):
    routes[assigned_robot].append(city_index)

# Apply 2-opt to optimize each route
optimized_routes = {}
total_travel_cost = 0

for robot_index, route in routes.items():
    optimized_route = two_opt(route + [depots[robot_index]])  # return back to depot
    travel_cost = sum(calculate_distance(optimized_route[i], optimized_route[i - 1]) for i in range(1, len(optimized_route)))
    optimized_routes[robot_index] = (optimized_route, travel_cost)
    total_travel_cost += travel

# Output the results
for robot_index, (route, cost) in optimized_routes.items():
    print(f"Robot {robot_index} Tour: {route}")
    print(f"Robot {robot_index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")