import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# List of city coordinates
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
          (155, 185), (139, 182)]

# Number of robots
num_robots = 4

# Calculate pairwise distances
city_locs = np.array(cities)
dist_matrix = cdist(city_locs, city_locs)

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Clustering the cities (excluding the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locs[1:])
labels = kmeans.labels_

# Initializing tours for each robot
tours = {i: [0] for i in range(num_robots)}

# Assigning cities to each robot based on clusters
for i, label in enumerate(labels):
    tours[label].append(i + 1)

# Ensuring each tour ends back at the depot
for i in range(num_robots):
    tours[i].append(0)

# Print initial solution
for i in range(num_robots):
    print(f"Robot {i} Initial Tour: {tours[i]}")
    print(f"Robot {i} Initial Total Travel Cost: {calculate_tour_cost(tours[i])}")

# Simple local search - 2-opt to optimize the tours
def two_opt(tour):
    """Attempts to improve the tour by reversing segments."""
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent nodes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Optimizing each robot's tour
for i in range(num_robots):
    optimized_tour = two_opt(tours[i])
    tours[i] = optimized_tour
    print(f"Robot {i} Optimized Tour: {optimized_tour}")
    print(f"Robot {i} Optimized Total Travel Cost: {calculate_tour_cost(optimized_tour)}")

# Calculate the maximum travel cost among all robots
max_cost = max(calculate_tour_cost(tours[i]) for i in range(num_robots))
print(f"Maximum Travel Cost: {max_cost}")