import math

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of city coordinates
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
    (93, 15)
]

# Nearest Neighbor approach to generate an initial tour starting from the depot city
def nearest_neighbor(cities, start):
    tour = [start]
    remaining = set(range(1, len(cities)))
    
    while remaining:
        current_city = tour[-1]
        next_city = min(remaining, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining.remove(next_city)
    
    tour.append(start)  # returning to depot
    return tour

# Calculate the total cost of the tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Get tour using the nearest neighbor
tour = nearest_neighbor(cities, 0)
cost = tour_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)