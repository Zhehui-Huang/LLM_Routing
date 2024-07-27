import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
num_cities = len(cities)
dist_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = calc_distance(cities[i], cities[j])

# Nearest Neighbor method
def nearest_neighbor(start=0):
    unvisited = set(range(1, num_cities))
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # returning to the depot
    return tour

# Generating tour
tour = nearest_neighbor()

# Calculating total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour)-1):
    dist = dist_matrix[tour[i]][tour[i+1]]
    total_cost += dist
    max_distance = max(max_distance, dist)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")