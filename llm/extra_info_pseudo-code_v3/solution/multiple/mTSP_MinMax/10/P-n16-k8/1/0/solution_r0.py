import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from copy import deepcopy

# Define the city coordinates based on the provided locations
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Convert cities to matrix
cities_coords = np.array(list(cities.values()))

# Number of robots
num_robots = 8

# Compute pairwise distances
dist_matrix = cdist(cities_coords, cities_coords, metric='euclidean')

def calculate_route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))

def random_greedy_clustered_tour(start, clusters):
    tour = [start]
    for cluster in clusters:
        np.random.shuffle(cluster)
        tour.extend(cluster)
    tour.append(start)
    return tour

def two_opt_single_route(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)):
                if j-i == 1: continue  # Skip adjacent nodes
                new_route = route[:] 
                new_route[i:j] = route[j-1:i-1:-1]  # Reverse part of the route
                if calculate_route_cost(new_route) < calculate_route_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

# Initialize clusters using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities_coords[1:])  # exclude depot
clusters = {i: [] for i in range(num_robots)}

for i, label in enumerate(kmeans.labels_, start=1):
    clusters[label].append(i)

# Generate initial tours using clustered cities
tours = [random_greedy_clustered_tour(0, [clusters[i]]) for i in range(num_robots)]

# Improvement: apply 2-opt on each of the generated tours
improved_tours = [two_opt_single_route(tour) for tour in tours]

# Calculate the travel cost for each tour
tour_costs = [calculate_route_cost(tour) for tour in improved_tours]

# Find the maximum travel cost
max_cost = max(tour_costs)

# Print the results
for i, (tour, cost) in enumerate(zip(improved_tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")