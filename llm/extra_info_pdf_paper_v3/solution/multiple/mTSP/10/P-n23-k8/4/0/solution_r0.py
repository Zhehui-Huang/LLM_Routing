import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Constants
num_robots = 8
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

def calc_distance_matrix(coords):
    # Create a matrix of Euclidean distances between each pair of points
    return distance_matrix(coords, coords)

def create_initial_solution(num_robots, city_coords):
    # Clustering cities for each robot by KMeans
    cities = np.array(city_coords[1:])  # Exclude the depot for clustering
    kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(cities)
    clusters = kmeans.labels_
    tours = {i: [0] for i in range(num_robots)}  # Start each tour at the depot
    
    for city_index, cluster_label in enumerate(clusters):
        tours[cluster_label].append(city_index + 1)  # Adjust city index (+1) because we excluded depot originally
    
    # Append the depot back to each tour
    for tour in tours.values():
        tour.append(0)
    return tours

def two_opt(route, distance_matrix):
    # Two-opt optimization to refine the path
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1: continue  # skip consecutive nodes
                new_route = route[:]
                new_route[i:j+1] = route[j:i-1:-1]  # reverse section of route
                if sum(distance_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)) > \
                   sum(distance_matrix[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)):
                    best = new_route
                    improved = True
        route = best
    return route

# Calculate distances
dist_matrix = calc_distance_matrix(city_coords)

# Generate an initial tour allocation for the robots
initial_tours = create_initial_solution(num_robots, city_coords)

# Optimize each tour
optimized_tours = {}
overall_cost = 0
for robot_id, tour in initial_tours.items():
    optimized_tour = two_opt(tour, dist_matrix)
    optimized_tours[robot_id] = optimized_tour
    tour_cost = sum(dist_matrix[optimized_tour[i]][optimized_tour[i + 1]] for i in range(len(optimized_tour) - 1))
    print(f'Robot {robot_id} Tour: {optimized_tour}')
    print(f'Robot {robot_id} Total Travel Cost: {tour_cost}')
    overall_cost += tour_cost

print(f'Overall Total Travel Cost: {overall_cost}')