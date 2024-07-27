import math

# Coordinates of the cities
cities = [
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

# Number of cities to visit including the depot
k = 10

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate all pairwise distances between cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def nearest_neighbor_tour(start_city):
    unvisited = set(range(len(cities)))
    tour = [start_city]
    unvisited.remove(start_city)
    
    while len(tour) < k:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distances[last_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    # Returning to the depot
    tour.append(start_city)
    return tour

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i+1]]
    return total_distance

# Get the tour starting from the depot city 0
tour = nearest_neighbor_tour(0)
total_distance = calculate_total_distance(tour)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")