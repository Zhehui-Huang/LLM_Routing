import numpy as np

# Coordinates of cities including the depot
coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Creating the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

def nearest_neighbor_tour(start_city):
    unvisited_cities = set(range(num_cities))
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the depot
    return tour

# Get the tour
tour = nearest_neighbor_tour(0)

# Calculate the total distance of the tour
total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Result output
print("Tour:", tour)
print("Total travel cost:", total_distance)