import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Define the city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Initialize data array and k-means
X = np.array(cities)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(X)

# Cluster centers
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Function to calculate Euclidean distance
def calculate_tour_cost(tour, cities):
    tour_cost = 0
    for i in range(len(tour)-1):
        tour_cost += np.linalg.norm(np.array(cities[tour[i]]) - np.array(cities[tour[i+1]]))
    return tour_cost

# Function to distribute cities among robots based on clusters
def assign_cities_to_robots(labels, num_robots):
    tours = [[] for _ in range(num_robots)]
    for idx, label in enumerate(labels):
        tours[label].append(idx)
    return tours

# Distribute cities to each robot based on clusters
robots_tours = assign_cities_to_robots(labels, num_robots)

# Calculate the tour and respective costs
total_cost = 0
for idx, tour in enumerate(robots_tours):
    # Add the depot to the start and appropriate end city
    depot_start = tour[0]  # Start at the depot city
    tour.insert(0, depot_start)
    
    # Calculate the cost of the full tour
    cost = calculate_tour_cost(tour, cities)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")