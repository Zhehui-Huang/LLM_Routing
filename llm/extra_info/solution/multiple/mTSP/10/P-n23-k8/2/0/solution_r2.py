import numpy as np
from sklearn.cluster import KMeans
import itertools

# Given city coordinates excluding the depot
city_coordinates = [ (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
                     (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
                     (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
                     (45, 35), (32, 39), (56, 37) ]

# Define the number of robots
num_robots = 8

# Create the distance matrix including the depot
coordinates = [(30, 40)] + city_coordinates
distance_matrix = distance_matrix(coordinates, coordinates)

# Clustering cities based on their location to partition the TSP among robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Prepare the tours for each robot
robots_tours = [[] for _ in range(num_robots)]
for city in range(1, len(coordinates)):  # Start from 1 to exclude the depot from routing
    robots_tours[labels[city]].append(city)

# Function to compute the travel cost of a tour
def compute_tour_cost(tour):
    cost = distance_matrix[0][tour[0]]  # From depot to first city in the tour
    for i in range(len(tour) - 1):
        cost += distance_manager[tour[i]][tour[i + 1]]
    cost += distance_manager[tour[-1]][0]  # Return to depot
    return cost

# Calculate the tour for each robot and the corresponding costs
total_cost = 0
for i, tour in enumerate(robots_tours):
    complete_tour = [0] + tour + [0]  # Start and end at the depot
    tour_cost = compute_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {complete_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

# Output the overall cost
print(f"Overall Total Travel Cost: {total_cost}")