import math

# List of city coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Heuristic: Nearest Neighbor Tour
def nearest_neighbor(n, start=0):
    unvisited = list(range(1, n))
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # complete the tour by returning to the depot
    return tour

# Compute metrics for the tour
def tour_metrics(tour, distance_matrix):
    total_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_edge = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_length, max_edge

# Initialize tour
tour = nearest_neighbor(n)
total_distance, max_distance = tour_metrics(tour, distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")