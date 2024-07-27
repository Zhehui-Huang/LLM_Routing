import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

def calculate_travel_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def two_opt_route(route, coordinates):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route)):
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_travel_cost(new_route) < calculate_travel_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

def assign_to_robots(n_robots, coordinates):
    kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates[1:])
    robot_tours = {i: [] for i in range(n_robots)}
    for idx, label in enumerate(kmeans.labels_):
        robot_tours[label].append(idx + 1)  # +1 to adjust index (city 0 is depot)
    
    for key in robot_tours:
        robot_tours[key] = [0] + robot_tours[key] + [0]  # Start and end at depot
    return robot_tours

def main(coordinates):
    n_robots = 4

    # Cluster cities and assign initial routes to robots
    robot_tours = assign_to_robots(n_robots, coordinates)

    # Optimize each route using 2-opt
    for robot in robot_tours:
        optimized_route = two_opt_route(robot_tours[robot], coordinates)
        robot_tours[robot] = optimized_route

    # Calculate and print the travel cost for each tour
    max_cost = 0
    for robot in robot_tours:
        cost = calculate_travel_cost(robot_tours[robot])
        print(f"Robot {robot} Tour: {robot_tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {cost:.2f}")
        max_cost = max(max_cost, cost)
    
    print(f"Maximum Travel Cost: {max_cost:.2f}")

# Run the main algorithm
main(coordinates)