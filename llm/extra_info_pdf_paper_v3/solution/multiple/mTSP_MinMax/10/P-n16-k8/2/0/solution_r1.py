import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclidean(cities[i], cities[j])
    return distance_matrix

def initialize_clusters(num_robots, cities):
    kmeans = KMeans(n_clusters=num_robots)
    clusters = kmeans.fit_predict(cities)
    return clusters

def two_opt(tour, dist_matrix):
    best_distance = calculate_tour_length(tour, dist_matrix)
    best_tour = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)-1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_tour_length(new_tour, dist_matrix)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return best_tour

def calculate_tour_length(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Setup environment
num_robots = 8
dist_matrix = calculate_distance_matrix(cities)

# Cluster cities into initial tours for each robot
initial_clusters = initialize_clusters(num_robots, cities[1:])  # excluding the depot city
tours = [[] for _ in range(num_robots)]
for i, cluster_index in enumerate(initial_clusters):
    tours[cluster_index].append(i + 1)  # city indices shifted by 1 due to depot

# Add the depot (city 0) to start and end of each tour
final_tours = [[0] + tour + [0] for tour in tours]

# Optimize each tour with a simple 2-opt algorithm
optimized_tours = [two_opt(tour, dist_matrix) for tour in final_tours]
tour_costs = [calculate_tour_length(tour, dist_matrix) for tour in optimized_tours]

# Determine the maximum travel cost across all tours
max_travel_cost = max(tour_costs)

# Output results
for i, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Hagazines nf Cost: {max_travel_cost}")