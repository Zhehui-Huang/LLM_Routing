import numpy as np
import itertools

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

# Compute Euclidean distance between all pairs of cities
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))

# Approximating MTSP using K-means clustering and nearest neighbor algorithm
from sklearn.cluster import KMeans

num_robots = 4

# Determine clusters
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])  # Exclude depot for clustering
clusters = kmeans.labels_

# Initialize tours
tours = [[] for _ in range(num_robots)]
for i, cluster in enumerate(clusters):
    tours[cluster].append(i + 1)  # city index adjusted for 0-indexed cities in clusters

# Function to calculate total cost of a tour
def tour_cost(tour):
    total_cost = distances[0, tour[0]]  # From depot to first city in tour
    for i in range(1, len(tour)):
        total_cost += distances[tour[i-1], tour[i]]
    total_cost += distances[tour[-1], 0]  # Return to depot
    return total_cost

# Complete tours starting/ending at depot
completed_tours = [[0] + tour + [0] for tour in tours]

# Calculate tour costs
total_costs = [tour is not None and tour_cost(tour) or 0 for tour in tours]
overall_total_cost = sum(total_costs)

# Output
for i in range(num_robots):
    print(f"Robot {i} Tour: {completed_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")