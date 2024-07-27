import math

# Define the cities as tuples of (x, y) coordinates
cities = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Nearest Neighbor heuristic to find a TSP tour
def nearest_neighbor_tour(start_city):
    unvisited = set(range(len(cities)))  # use a set for unvisited cities
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the starting (depot) city
    return tour

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(1, len(tour)):
        total_dist += distance(cities[tour[i-1]], cities[tour[i]])
    return total_dist

# Run the Nearest Neighbor algorithm from the depot city (index 0)
tour = nearest_neighbor_tour(0)
total_travel_cost = calculate_total_distance(tour)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)