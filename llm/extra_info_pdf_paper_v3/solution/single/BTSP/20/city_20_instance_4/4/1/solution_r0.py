import numpy as np

# Define the coordinates of the cities
coordinates = np.array([
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
])

# Calculate the Euclidean distance between all pairs of cities
def distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = np.linalg.norm(coords[i] - coords[j])
    return dist_matrix

dist_matrix = distance_matrix(coordinates)

# Using a simple heuristic to construct a tour that minimizes the maximum distance
# This is a variation of the nearest neighbor algorithm prioritizing shorter maximum links
def greedy_tour(dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(1, n))
    tour = [0]
    max_edge = 0

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[last][x])
        max_edge = max(max_edge, dist_matrix[last][next_city])
        tour.append(next_city)
        unvisited.remove(next_city)

    # Close the tour to return to the depot
    final_leg = dist_matrix[tour[-1]][0]
    max_edge = max(max_edge, final_leg)
    tour.append(0)
    
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_edge

# Get the tour
tour, total_cost, max_edge = greedy_tour(dist_matrix)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge)