import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

def greedy_tsp_tour(start_city, cities_to_visit, distance_matrix):
    tour = [start_city]
    current_city = start_city
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def two_opt(tour, distance_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j-1]][tour[j]] > \
                   distance_matrix[tour[i-1]][tour[j-1]] + distance_matrix[tour[i]][tour[j]]:
                    tour[i:j] = tour[j-1:i-1:-1]
                    improvement = True
    return tour

# Cities coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
])

num_robots = 8
distance_matrix = calculate_distance_matrix(cities)

# K-Means Clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])  # Skipping the depot
clusters = [[] for _ in range(num_robots)]
for i, label in enumerate(kmeans.labels_):
    clusters[label].append(i+1)  # City index adjusted for 0-start indexing

# Constructing initial tours
tours = []
for cluster in clusters:
    if cluster:
        tour = greedy_tsp_tour(0, cluster, distance_matrix)
        optimized_tour = two_opt(tour, distance_matrix)
        tours.append(optimized_tour)

# Calculate the costs
tour_costs = [calculate_tour_cost(tour, distance_matrix) for tour in tours]
max_cost = max(tour_costs)

for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")