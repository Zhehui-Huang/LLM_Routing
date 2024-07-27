import math

# Definition of cities coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    dx = coordinates[city_a][0] - coordinates[city_b][0]
    dy = coordinates[city_a][1] - coordinates[city_b][1]
    return math.sqrt(dx * dx + dy * dy)

# Function to find the nearest neighbor tour starting from a given start city
def nearest_neighbor_tsp(start_city):
    n = len(coordinates)
    unvisited = list(range(n))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # complete the tour by returning to the start city
    return tour

# Compute the TSP tour using the nearest neighbor heuristic
tour = nearest_neighbor_tsp(0)
total_travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_distance_between_cities = max(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")