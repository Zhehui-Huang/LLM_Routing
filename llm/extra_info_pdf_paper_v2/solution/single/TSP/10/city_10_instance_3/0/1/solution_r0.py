import numpy as np

# City coordinates
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), 
               (8, 62), (74, 56), (85, 71), (6, 76)]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initial tour using the nearest neighbor heuristic
def nearest_neighbor_tour(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unavailable_exceptions=False, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to the start
    return tour

# Function to calculate the total distance of the tour
def calculate_total_distance(tour):
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_distance

# Generate an initial tour
initial_tour = nearest_neighbor_tour()
initial_cost = calculate_total_distance(initial_tour)

# Function to perform a simple 2-opt swap
def perform_2opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

# 2-opt heuristic to improve the tour
def two_opt(tour):
    improvement = True
    best_distance = calculate_total_distance(tour)
    best_tour = tour[:]
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = perform_2opt_swap(tour, i, k)
                new_cost = calculate_total_distance(new_tour)
                if new_cost < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_cost
                    improvement = True
        tour = best_tour
    return best_tour, best_distance

# Improve the initial solution
best_tour, best_cost = two_opt(initial_tour)

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)