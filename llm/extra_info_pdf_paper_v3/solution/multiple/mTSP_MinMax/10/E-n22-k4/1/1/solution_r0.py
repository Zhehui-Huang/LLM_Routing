import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# City coordinates including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4

# Create distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def solve_mtsp(coordinates, num_robots, dist_matrix):
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # Exclude the depot city
    clusters = kmeans.labels_
    
    robots_tours = [[] for _ in range(num_robots)]
    for i, cluster_id in enumerate(clusters, start=1):  # Start from 1 to skip depot
        robots_tours[cluster_id].append(i)
    
    # Prepend and append the depot city (0) to each tour
    for tour in robots_tours:
        tour.insert(0, 0)
        tour.append(0)
    
    # Calculate the costs
    costs = [calculate_tour_cost(tour, dist_matrix) for tour in robots_tours]
    max_cost = max(costs)
    
    return robots_tours, costs, max_cost

# Calculate the tours and costs
tours, costs, max_cost = solve_mtsp(coordinates, num_robots, dist_matrix)

# Output the results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")