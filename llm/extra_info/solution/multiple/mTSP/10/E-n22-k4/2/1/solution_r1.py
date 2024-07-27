import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from sympy.utilities.iterables import multiset_permutations

# Coordinates of the cities including the depot
city_coords = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Number of robots
num_robots = 4

# Function to calculate the round trip for a tour
def calculate_tour_cost(tour):
    return sum(euclidean(city_coords[tour[i]], city_coords[tour[i + 1]]) for i in range(len(tour) - 1))

# Function to find the shortest TSP route for a cluster of cities
def tsp_route(cities):
    best_route = None
    min_cost = float('inf')
    cities = list(cities)
    
    for perm in multiset_permutations(cities):
        route = [0] + list(perm) + [0]
        cost = calculate_tour_cost(route)
        if cost < min_cost:
            min_cost = cost
            best_route = route
    
    return best_route, min_select_cost

# Cluster the cities (excluding the depot) into num_robots clusters using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords[1:])
clusters = {i: [] for i in range(num_robots)}
for i, label in enumerate(kmeans.labels_):
    clusters[label].append(i + 1)  # +1 to adjust index since city 0 is not included in clustering

# Determine the optimum tour for each robot
tours = []
total_cost = 0

for i, cluster in clusters.items():
    tour, tour_cost = tsp_route(cluster)
    tours.append((tour, tour_cost))
    total_cost += tour_cost

# Outputting the results
for index, (tour, cost) in enumerate(tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")