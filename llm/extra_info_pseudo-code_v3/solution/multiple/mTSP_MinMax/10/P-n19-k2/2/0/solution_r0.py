import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

def euclidean_distance(a, b):
    return np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2))

def initialize_clusters(coordinates, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coordinates)
    return kmeans.labels_

def greedy_tour(initial_city, cities, distance_matrix):
    tour = [initial_city]
    current_city = initial_city
    unvisited = set(cities)
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(initial_city)  # return to the depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def two_opt(tour, distance_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, distance_matrix) < calculate_tour_cost(best, distance_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
cities = list(range(1, 19))  # excluding the depot city

# Compute distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(19)] for i in range(19)]

# Cluster cities (excluding the depot)
clusters = initialize_clusters([coordinates[i] for i in cities], num_robots)

# Assign cities to robots based on clusters
robot_tours = [[] for _ in range(num_robots)]
for city, cluster in zip(cities, clusters):
    robot_tours[cluster].append(city)

# Generate initial greedy tours for each robot
for i in range(num_robots):
    robot_tours[i] = greedy_tour(0, robot_tours[i], distance_matrix)
    robot_tours[i] = two_opt(robot_tours[i], distance_matrix)

# Calculate tour costs and find maximum travel cost
tour_costs = [calculate_tour_cost(tour, distance_matrix) for tour in robot_tours]
max_cost = max(tour_costs)

# Print final tours and costs
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")