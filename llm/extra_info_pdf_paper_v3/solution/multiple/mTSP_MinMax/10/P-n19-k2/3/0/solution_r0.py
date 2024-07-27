import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from itertools import permutations

# Given data
city_coords = np.array([
    [30, 40], [37, 52], [49, 43], [52, 64], [31, 62], [52, 33], [42, 41], 
    [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 27], 
    [37, 69], [61, 33], [62, 63], [63, 69], [45, 35]])

# Define number of robots
num_robots = 2
depot = 0

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Create distance matrix
dist_matrix = distance_matrix(city_coords, city_coords)

# Clustering cities (exempting the depot) using K-Means
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords[1:])  # exclude depot
labels = kmeans.labels_

# Assign cities to each robot
robot_assignments = {i: [0] for i in range(num_robots)}  # initialize with depot
for i, label in enumerate(labels, start=1):
    robot_assignments[label].append(i)
for key in robot_assignments.keys():
    robot_assignments[key].append(0)  # return to depot

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, dist_matrix) < calculate_tour_cost(best, dist_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Optimize each robot's tour using two_opt
optimized_tours = {}
for robot, tour in robot_assignments.items():
    optimized_tours[robot] = two_opt(tour)

# Calculate the costs
costs = {}
for robot, tour in optimized_tours.items():
    costs[robot] = calculate_tour_cost(tour, dist_matrix)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]:.2f}")

max_cost = max(costs.values())
print(f"Maximum Travel Cost: {max_cost:.2f}")