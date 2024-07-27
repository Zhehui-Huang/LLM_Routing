import numpy as np

def calculate_euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = calculate_euclidean_distance(cities[i], cities[j])
    return distance_matrix

def nearest_neighbor_tour(start, distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to the depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1], tour[i]]
    return total_cost

# Define the cities as tuples
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Get the distance matrix
distance_matrix = create_distance_matrix(cities)

# Generate a tour using the nearest neighbor heuristic
initial_tour = nearest_neighbor_tour(0, distance_matrix)

# Calculate tour cost
tour_cost = calculate_tour_cost(initial_tour, distance_matrix)

print("Tour:", initial_tour)
print("Total travel cost:", tour_cost)