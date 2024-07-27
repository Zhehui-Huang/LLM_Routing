import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Input data: City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Number of robots
num_robots = 2

def distance_matrix(coordinates):
    """ Compute the Euclidean distance matrix. """
    num_cities = len(coordinates)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])
    return dist_matrix

def calculate_tour_cost(tour, dist_matrix):
    """ Calculate the cost of a tour based on the distance matrix. """
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def two_opt_swap(tour):
    """ Tries to improve tour by performing 2-opt swaps. """
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, dist_matrix) < calculate_tour_cost(best, dist_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Remove the depot city and perform clustering
client_cities = list(cities.keys())[1:]  
city_positions = np.array([cities[city] for city in client_cities])

# Perform clustering using K-means
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_positions)
clusters = {i: [] for i in range(num_robots)}
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(client_cities[idx])

# Distance matrix including the depot
full_coordinates = np.array([cities[city] for city in cities])
dist_matrix = distance_matrix(full_coordinates)

# Assign tours initialized from clusters and optimize them
tours = {}
for robot in clusters:
    tour = [0] + clusters[robot] + [0]
    tour = two_opt_swap(tour)
    tours[robot] = tour

# Calculate costs and find the maximum
max_cost = 0
for robot, tour in tours.items():
    cost = calculate_tour_cost(tour, dist_matrix)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")
    max_cost = max(max_cost, cost)

print(f"Maximum Travel Cost: {max_cost:.2f}")