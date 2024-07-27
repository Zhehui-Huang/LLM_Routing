import math

# Function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of cities with coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 25)
]

# Nearest neighbor TSP solver
def nearest_neighbor_tsp(cities):
    n = len(cities)
    start = 0  # starting point (depot)
    unvisited = set(range(1, n))
    tour = [start]
    current_city = start
    
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        total_cost += calculate_distance(cities[current_city], cities[next_city])
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    
    # Add the cost and path to return to the depot
    total_cost += calculate_distance(cities[current_city], cities[start])
    tour.append(start)
    
    return tour, total_cost

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")