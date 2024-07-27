from math import sqrt
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from concorde.tsp import TSPSolver

# Define the coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Define the number of robots and their respective depot start and end points
num_robots = 2
depots = [0, 1]

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# Cluster the cities (excluding depots) into two clusters corresponding to each robot's tour
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[2:])  # skip the depot coordinates in clustering
labels = kmeans.labels_

# Create tours based on clusters and depots
tours = {i: [depots[i]] for i in range(num_robots)}
for idx, label in enumerate(labels):
    tours[label].append(idx + 2)  # re-adjust indices to match the full set with depots

# Each robot returns to their depot after completing their cluster
for robot in tours:
    tours[robot].append(depots[robot])

# Optimize each tour using Concorde TSP Solver
def optimize_tour(tour):
    # Extract coordinates for the selected tour
    sub_coords = np.array([coordinates[i] for i in tour])
    solver = TSPSolver.from_data(sub_coords[:, 0], sub_coords[:, 1], norm="EUC_2D")
    solution = solver.solve()
    
    optimized_tour_indices = [tour[i] for i in solution.tour]
    # Ensure the tour starts and ends at the depot
    optimized_tour_indices.append(optimized_tour_indices[0])
    return optimized_tour_indices

optimized_tours = {}
total_travel_cost = 0

for robot in tours:
    optimized_tours[robot] = optimize_tour(tours[robot])
    tour_distance = sum(calc_distance(optimized_tours[robot][i], optimized_tours[robot][i + 1]) for i in range(len(optimized_tours[robot]) - 1))
    print(f"Robot {robot} Tour: {optimized_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_distance:.2f}")
    total_travel_cost += tour_distance

print(f"Overall Total Travel Cost: {total