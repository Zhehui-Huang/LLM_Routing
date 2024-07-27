import numpy as np
from scipy.spatial import distance_matrix

# Coordinates of cities (index 0 is the depot)
coordinates = np.array([
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
])

# Compute the Euclidean distance matrix
distances = distance_matrix(coordinates, coordinates)

# Nearest Neighbor Heuristic
def nearest_neighbor_tour(start, distances):
    n = len(distances)
    visited = np.zeros(n, dtype=bool)
    tour = [start]
    visited[start] = True

    current = start
    while len(tour) < n:
        next_city = np.argmin(distances[current] + (visited * 1e9))  # large number to exclude visited
        visited[next_city] = True
        tour.append(next_city)
        current = next_city

    tour.append(start)  # return to the depot
    return tour

# Calculate total travel cost of a tour
def calculate_total_distance(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Get the tour starting from the depot city 0
tour = nearest_neighbor_tour(0, distances)

# Total distance of the tour
total_distance = calculate_total_distance(tour, distances)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_distance)