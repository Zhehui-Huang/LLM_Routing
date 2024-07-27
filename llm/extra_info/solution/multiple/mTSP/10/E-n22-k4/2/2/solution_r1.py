import numpy as thenp
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of cities including the depot (index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Creating the distance matrix
def create_distance_matrix(coords):
    dist_matrix = np.zeros((len(coords), len(coords)))
    for i in range(len(coords)):
        for j in range(len(coords)):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = create_distance_matrix(coordinates)

# Clustering cities for 4 robots
kmeans = KMeans(n_clusters=4)
clusters = kmeans.fit_predict(coordinates[1:])  # exclude depot

# Organizing cities by robot
robot_cities = [[] for _ in range(4)]
for i, cluster in enumerate(clusters):
    robot_cities[cluster].append(i + 1)  # shift index for cities (since we excluded depot)

from itertools import permutations

# Helper function to calculate the cost of a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Searching for the shortest path using a naive approach
def find_optimal_tour(cities, dist_matrix):
    depot = 0
    min_cost = float('inf')
    best_path = []
    cities = [depot] + cities + [depot]
    for perm in permutations(cities[1:-1]):
        current_path = [depot] + list(perm) + [depot]
        current_cost = calculate_tour_cost(current_path, dist_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    return best_path, min_cost

total_cost = 0
print("Result Format:")
for i, cities in enumerate(robot_cities):
    tour, cost = find_optimal_tour(cities, distance_matrix)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")