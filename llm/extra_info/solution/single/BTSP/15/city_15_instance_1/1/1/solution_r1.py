import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate an initial feasible tour by adding the nearest unvisited city
def nearest_neighbor_tour(start):
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # Complete the tour by returning to the start
    return tour

# Calculate maximum and total distance of the tour
def calculate_distances(tour):
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_leg_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_leg_distance

# Compute the tour using the nearest neighbor heuristic
initial_tour = nearest_neighbor_tour(0)
total_cost, max_leg_distance = calculate_distances(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")