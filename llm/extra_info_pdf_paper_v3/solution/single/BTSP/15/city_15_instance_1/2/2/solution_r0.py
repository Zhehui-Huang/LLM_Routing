import math

# Definitions of cities' coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Finding a tour that minimizes the maximum distance between consecutive cities
def find_min_max_tour(start):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start
    max_leg_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        max_leg_distance = max(max_leg_distance, distance_matrix[current][next_city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)

    # Close the tour
    tour.append(start)
    max_leg_distance = max(max_leg_distance, distance_matrix[current][start])

    # Total travel cost
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost, max_leg_distance

# Solve the problem
tour, total_cost, max_distance = find_min_max_tour(0)

# Output
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))