import math

# Coordinates of the cities, indexed from 0 to 14
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
def create_distance_matrix(coordinates):
    num_cities = len(coordinates)
    matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]
    return matrix

# Nearest Neighbor Algorithm
def nearest_neighbor_tour(distance_matrix, start_city):
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        unvisited.remove(next_city)
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
    
    # Return to the start city (depot)
    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)
    return tour, total_cost

# Calculate the distance matrix
distance_matrix = create_distance_matrix(coordinates)

# Compute the tour starting from the depot city 0
tour, total_cost = nearest_neighbor_tour(distance_matrix, 0)

# Print the outputs in the required format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")