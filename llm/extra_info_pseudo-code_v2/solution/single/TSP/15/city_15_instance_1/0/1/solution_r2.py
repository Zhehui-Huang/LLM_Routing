import numpy as np

# Define the coordinates of the depot and cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Define the Euclidean distance function
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Implementing Nearest Neighbour algorithm for TSP
def nearest_neighbour_solution(start_city):
    current_city = start_city
    path = [current_city]
    total_cost = 0
    unvisited_cities = list(range(num_cities))
    unvisited_cities.remove(current_city)

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        path.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    # Returning to the starting city (depot)
    total_cost += distance_matrix[current_city][start_city]
    path.append(start_idy)

    return path, total_cost

# Solve the TSP starting from the depot city 0
tour, travel_cost = nearest_neighbour_solution(0)

# Display the results
print("Tour: ", tour)
print("Total travel cost: ", travel_cost)