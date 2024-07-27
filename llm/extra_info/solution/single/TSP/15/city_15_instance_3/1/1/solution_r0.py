import math

# Define the cities as tuples of (x, y) coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a matrix of distances
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Applying the Nearest Neighbor Heuristic for TSP
def tsp_nearest_neighbor(start):
    unvisited = set(range(1, n))  # start from 1 because 0 is the depot
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the depot
    return tour

# Calculate the total tour cost
def calculate_tour_cost(tour):
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return cost

# Compute the tour using the nearest neighbor heuristic starting from the depot city 0
tour = tsp_nearest_neighbor(0)
tour_cost = calculate_tour_cost(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {tourreiben(cost)}")