import math

# Coordinates for the depot and other cities
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73), 
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Building the distance matrix
def build_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')  # Infinite distance to self to avoid self-loop
    return distance_matrix

# Nearest neighbor algorithm to find the TSP tour
def nearest_neighbor_tsp(distance_matrix, start_city):
    n = len(distance_matrix)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city) # Return to the starting city (depot)
    return tour

# Calculate the total travel cost of a given tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost

# Solve the TSP
distance_matrix = build_distance_matrix(cities)
tour = nearest_neighbor_tsp(distance_matrix, 0)
total_cost = calculate_toplevel_cost(tour, distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")