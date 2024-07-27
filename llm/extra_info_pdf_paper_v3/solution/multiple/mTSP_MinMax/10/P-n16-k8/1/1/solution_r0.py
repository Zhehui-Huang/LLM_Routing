import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
    return distances

def initial_solution(clusters, n_robots):
    tours = [[] for _ in range(n_robots)]
    for idx, cluster in enumerate(clusters):
        tours[idx % n_robots].append(idx + 1)  # City indices are shifted by 1 because of the depot
    for tour in tours:
        tour.insert(0, 0)  # Start at the depot
        tour.append(0)     # End at the depot
    return tours

def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def compute_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Operation variables
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
n_robots = 8

# Calculate distances between cities
distances = calculate_distances(cities)

# Clustering cities (minus the depot city 0)
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(cities[1:])
cluster_labels = kmeans.labels_

# Initial solution based on clusters
tours = initial_solution(cluster_labels, n_robots)

# Calculation and optimization
max_cost = 0
for i in range(n_robots):
    min_change = True
    while min_change:
        min_change = False
        current_cost = compute_cost(tours[i], distances)
        for u in range(1, len(tours[i]) - 2):
            for v in range(u + 1, len(tours[i]) - 1):
                if u == 0 and v == len(tours[i]) - 1:
                    continue
                new_tour = two_opt_swap(tours[i], u, v)
                new_cost = compute_cost(new_tour, distances)
                if new_cost < current_cost:
                    tours[i] = new_tour
                    current_cost = new_cost
                    min_change = True
    
    total_cost = compute_cost(tours[i], distances)
    if total_cost > max_cost:
        max_cost = total_cost
    
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_cost}")

print(f"Maximum Travel Cost: {max_cost}")