import numpy as np

# Coordinates of each city including the depot
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39),
               (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate the distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = distance(coordinates[i], coordinates[j])

# Nearest Neighbor heuristic to generate a feasible tour
def nearest_neighbor(start=0):
    unvisited = list(range(1, n))
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[current, x])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # Return to depot
    return tour

# Calculate total travel cost of the tour
def calculate_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i], tour[i+1]]
    return total_cost

# 2-opt Swap Optimization
def two_opt(tour, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour, distance_matrix) < calculate_cost(tour, distance_matrix):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

# Find the initial tour and improve it
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour, distance_matrix)
total_cost = calculate_cost(optimized_tour, distance_matrix)

# Outputting the solution
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)