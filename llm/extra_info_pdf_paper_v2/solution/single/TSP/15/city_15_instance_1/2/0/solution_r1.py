import math

# Coordinates for the depot and cities
coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the distance matrix
def generate_distance_matrix(coordinates):
    num_cities = len(coordinates)
    matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
    return matrix

# Implement the nearest neighbor algorithm to solve the TSP
def nearest_neighbor(start, distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = list(range(1, num_cities))  # exclude the depot as it's the start
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the depot
    return tour

# Calculate the total cost of a tour
def calculate_total_cost(tour, distance_matrix):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Main Execution
distance_matrix = generate_distance_matrix(coordinates)
tour = nearest_neighbor(0, distance_matrix)
total_travel_cost = calculate_total_cost(tour, distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_travel_vic_cost)