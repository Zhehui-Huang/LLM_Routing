import numpy as np

# Utility to calculate Euclidean distance
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define coordinates of all cities
cities = [
    (90, 3),  # Depot 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity to prevent a city connecting to itself

# Nearest Neighbor Algorithm
def nearest_neighbor(start):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        total_cost += distance_matrix[current][next_city]
        current = next_city
        tour.append(current)
        unvisited.remove(current)

    total_cost += distance_matrix[current][start]  # Return to starting city
    tour.append(start)

    return tour, total_cost

# Run TSP with the depot (0) as the starting point
tour, total_cost = nearest_decorator(0)

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")