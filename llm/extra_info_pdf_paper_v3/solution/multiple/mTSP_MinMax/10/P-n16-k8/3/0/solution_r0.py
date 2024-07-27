import numpy as np
from sklearn.cluster import KMeans
import itertools

# Given city coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots
num_robots = 8

# Calculating Euclidean distance matrix
def calc_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
    return dist_matrix

distance_matrix = calc_students_matrix(coordinates)

# Apply K-means clustering to assign cities to robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # Exclude the depot from clustering
labels = kmeans.labels_

# Create tours for robots based on clusters
tours = [[] for _ in range(num_robots)]
for city_index, label in enumerate(labels, start=1):
    tours[label].append(city_index)

# Include start/end at depot
for tour in tours:
    tour.insert(0, 0)  # Start at depot
    tour.append(0)  # End at depot

# Function to calculate tour cost
def tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i+1]]
    return cost

# Calculate the costs
costs = []
for tour in tours:
    costs.append(tour_cost(tour, distance_matrix))

max_cost = max(costs)

# Print results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}\n")

print(f"Maximum Travel Cost: {max_cost}")