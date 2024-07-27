import numpy as a np
from scipy.spatial.distance import pdist, squareform
import itertools

# City coordinates data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate the Euclidean pairwise distances matrix
dist_matrix = squareform(pdist(coordinates, 'euclidean'))

# Function to compute the route cost
def route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))

# Function to generate initial greedy clusters and tours
def initial_solution(num_robots):
    unvisited = set(range(1, len(coordinates)))  # city indices, excluding depot
    clusters = [set() for _ in range(num_robots)]

    # Simple clustering based on proximity to depot
    for i in sorted(unwritten, key=lambda x: dist_matrix[0][x]):
        nearest_robot = min(range(num_robots), key=lambda k: sum(dist_matrix[j][0] for j in clusters[k]))
        clusters[nearest_robot].add(i)
        if len(clusters[nearest_robot]) >= len(unvisited) // num_robots:
            break

    tours = []
    for cluster in clusters:
        # Sort each cluster's cities by proximity to each other, starting with the depot
        if cluster:
            tour = [0] + sorted(cluster, key=lambda x: dist_matrix[0][x])
            tour.append(0)  # Complete the tour by returning to the depot
            tours.append(tour)
        else:
            tours.append([0, 0])  # empty tour for any unused robot

    return tours

# Initial solution generation using the function
tours = initial_solution(num_robots)

# Calculate the travel cost of each tour and the maximum travel cost
tour_costs = {f"Robot {i} Total Travel Cost": route_cost(tour) for i, tour in enumerate(tours)}
tour_output = {f"Robot {i} Tour": tour for i, tour in enumerate(tours)}
max_travel_cost = max(tour_costs.values())

# Output the tours and costs
for key, value in tour_output.items():
    print(f"{key}: {value}")
for key, value in tour_costs.items():
    print(key, value)
print(f"Maximum Travel Cost: {max_travel_cost}")