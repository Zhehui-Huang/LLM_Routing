import numpy as np
from sklearn.cluster import KMeans

# Given city coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots, treat it like clusters
num_robots = 2

# Using K-Means to cluster cities into group based on proximity
kmeans = KMeans(n_clusters=num_robots, random_state=0)
assignments = kmeans.fit_predict(cities[1:])  # exclude depot for initial clustering

# Helper function to compute Euclidean distance
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# Initialize tours starting from the depot
tours = [[0] for _ in range(num_robots)]

# Assign cities to each robot based on clustering
for i, cluster_id in enumerate(assignments):
    tours[cluster_id].append(i + 1)  # city indices adjusted by +1 due to depot

# Append depot to end of each tour to return to start
for tour in tours:
    tour.append(0)

# Define function to calculate total travel cost of a tour
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Calculate and print each robot's tour and costs
max_cost = 0
for i in range(num_robots):
    tour_cost = calculate_tour_cost(tours[i], cities)
    max_cost = max(max_cost, tour_cost)
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel that any robot has to take: {max_cost}")