import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities coordinates
cities_coordinates = [
    (30, 56),  # City 0
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Number of cities
n_cities = len(cities_coordinates)

# Create distance matrix
distances = [
    [euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for j in range(n_cities)]
    for i in range(n_cities)
]

def nearest_neighbor_tour(start_city):
    unvisited = set(range(n_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Returning to the depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Get the tour
tour = nearest_neighbor_tour(0)
total_cost, max_distance = calculate_tour_cost(tour, distances)

# Output the required information
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")