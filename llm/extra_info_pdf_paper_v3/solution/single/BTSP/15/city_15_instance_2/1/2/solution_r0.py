import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_distances(cities):
    num_cities = len(cities)
    distance_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
    return distance_matrix

def create_mst_tour(cities):
    distances = calculate_distances(cities)
    sparse_matrix = csr_matrix(distances)
    mst = minimum_spanning_tree(sparse_matrix).toarray()
    dmst = np.where(mst > 0, mst, distances)
    
    #Build tour from MST
    visited = [False] * len(cities)
    tour = []
    
    def visit(city):
        visited[city] = True
        tour.append(city)
        for next_city in np.argsort(dmst[city]):
            if not visited[next_city] and dmst[city][next_city] > 0:
                visit(next_city)
    
    visit(0)  # start at the depot city
    tour.append(0)  # return to depot
    
    return tour

def calculate_tour_metrics(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        d = distances[tour[i-1]][tour[i]]
        total_cost += d
        max_distance = max(max_drive, d)
    
    return tour, total_cost, max_distance

# City coordinates
cities = [
    (54, 87),  # Depot
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Solve the problem
tour = create_mst_tour(cities)
distances = calculate_distances(cities)
tour, total_cost, max_distance = calculate_tour_metrics(tour, distances)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")