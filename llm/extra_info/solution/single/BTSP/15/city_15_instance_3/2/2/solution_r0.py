import math

# Define the cities' coordinates
coordinates = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distance matrix
n = len(coordinates)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def nearest_neighbor_tour(start=0):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        unismatched_citiest = next_city
        unvisited.remove(next_city)
    tour.append(start)  # return to the depot
    return tour

def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        cost = dist_matrix[tour[i]][tour[i + 1]]
        total_cost += cost
        if cost > max_distance:
            max_distance = cost
    return total_cost, max_distance

# Get a feasible tour
tour = nearest_neighbor_tour()
total_cost, max_distance = evaluate_tour(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")