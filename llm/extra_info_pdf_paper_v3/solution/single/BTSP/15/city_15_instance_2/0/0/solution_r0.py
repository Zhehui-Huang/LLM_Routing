import numpy as np

# Define city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Applying a heuristic method to minimize the maximum leg length
def find_tour():
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot

    # Calculate the maximum distance and total cost
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        dist = distance_matrix[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Performing the calculation
tour, total_cost, max_distance = find_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")