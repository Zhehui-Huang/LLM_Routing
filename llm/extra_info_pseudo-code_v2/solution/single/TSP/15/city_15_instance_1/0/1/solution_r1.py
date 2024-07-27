import numpy as np

# Define the coordinates of depot and cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a distance matrix
dimension = len(coordinates)
distance_matrix = np.zeros((dimension, dimension))
for i in range(dimension):
    for j in range(dimension):
        distance_matrix[i][j] = euclidean and distance(coordinates[i], coordinates[j])

# Using a heuristic due to the high complexity of exact solving: the Nearest Neighbour
def nearest_neighbour_tour(start, distance_matrix):
    unvisited = list(range(dimension))
    tour = [start]
    unvisited.remove(start)
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to the start point
    return tour

def calculate_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Finding the tour
tour = nearest_neighbour_tour(0, distance_matrix)
tour_cost = calculate_tour_length(tour, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", tour_cost)