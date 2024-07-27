import numpy as np
from sklearn.cluster import KMeans

# Define the cities coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
])

# Function to calculate Euclidean distance between two points
def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# 2-opt algorithm
def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+2, len(route)):
                if j-i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(distance_matrix[new_route[k]][new_route[k+1]] for k in range(len(new_route)-1)) < sum(distance_matrix[best[k]][best[k+1]] for k in range(len(best)-1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Compute distance matrix
n_cities = len(coordinates)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            dist_matrix[i][j] = distance(coordinates[i], coordinates[j])

# K-Means Clustering to group cities for each robot
kmeans = KMeans(n_clusters=4, random_state=0).fit(coordinates[1:])  # Exclude depot
clusters = kmeans.labels_

# Initialize tours for each robot
tours = [[0] for _ in range(4)]  # Start each tour at the depot

# Add stops according to clusters
for i, cluster in enumerate(clusters, start=1):
    tours[cluster].append(i)

# Close the tours by returning to the depot
for tour in tours:
    tour.append(0)

# Optimize routes with 2-opt
optimized_tours = []
for tour in tours:
    optimized_tour = two_opt(tour, dist_matrix)
    optimized_tours.append(optimized_tour)

# Output results
overall_cost = 0
for index, tour in enumerate(optimized_tours):
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")