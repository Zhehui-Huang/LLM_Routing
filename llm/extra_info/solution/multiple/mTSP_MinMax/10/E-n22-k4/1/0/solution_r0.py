import numpy as np
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
from itertools import permutations

# City coordinates including the depot
coordinates = [
    (145, 215),  # Depot
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

n_robots = 4
depot = 0

# Step 1: Compute the distance matrix
coordinates = np.array(coordinates)
distances = squareform(pdist(coordinates, metric='euclidean'))

# Step 2: Cluster the cities (excluding the depot)
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates[1:])  # Excluding depot
labels = kmeans.labels_

# Step 3: Distribute cities to each robot
tours = {i: [depot] for i in range(n_robots)}
for city, label in enumerate(labels, start=1):
    tours[label].append(city)

# Ensuring each tour returns to the depot
for k in tours:
    tours[k].append(depot)

# Function to calculate the cost of a tour
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Calculate the travel cost for each tour
costs = {k: tour_cost(tours[k], distances) for k in tours}
max_cost = max(costs.values())

# Output the results
for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")