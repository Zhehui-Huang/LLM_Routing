import math
import random

# Coordinates of cities including the depot (index 0)
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = distance(cities[i], cities[j])
    return distances

# Function to find the total distance of a tour
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Simple initial tour generator using nearest neighbor heuristic
def initial_tour(cities):
    start_city = 0
    unvisited = list(range(1, len(cities)))
    tour = [start_city]
    while unvisited:
        current_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start_city)  # return to the depot
    return tour

# Lin-Kernighan Heuristic: simplified and adapted implementation
def lin_kernighan(cities):
    distance_matrix = create_distance_matrix(cities)
    tour = initial_tour(cities)
    initial_cost = tour_cost(tour, distance_matrix)

    # Implement the 2-opt step
    def two_opt_swap(opt_tour):
        best = opt_tour
        best_cost = tour_cost(best, distance_matrix)
        improved = True
        while improved:
            improved = False
            for i in range(1, len(opt_tour) - 2):
                for j in range(i + 2, len(opt_tour) - 1):
                    if j - i == 1:
                        continue
                    new_tour = opt_tour[:i] + opt_tour[i:j][::-1] + opt_tour[j:]
                    new_cost = tour_cost(new_tour, distance_matrix)
                    if new_cost < best_cost:
                        best = new_tour
                        best_cost = new_cost
                        improved = True
        return best
    
    improved_tour = two_opt_swap(tour)
    improved_cost = tour_cost(improved_tour, distance_matrix)

    return improved_tour, improved_cost

# Get the shortest tour and its cost using Lin-Kernighan heuristic
tour, cost = lin_kernighan(cities)

print("Tour:", tour)
print("Total travel cost:", round(cost, 2))