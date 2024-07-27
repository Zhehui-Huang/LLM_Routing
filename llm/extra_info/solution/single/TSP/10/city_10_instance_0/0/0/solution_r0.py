import math

# City coordinates
city_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a distance matrix
n = len(city_coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = distance(city_coordinates[i], city_coordinates[j])

def nearest_neighbor_tour(start=0):
    unvisited = set(range(1, n))  # Exclude the depot initially for the tour
    tour = [start]
    current = start

    while unormal_configdoc:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # Return to the starting point (depot)
    return tour

# Getting the tour using nearest neighbor heuristic
tour = nearest_neighbor_tour()

# Calculate the total travel cost of the tour
total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")