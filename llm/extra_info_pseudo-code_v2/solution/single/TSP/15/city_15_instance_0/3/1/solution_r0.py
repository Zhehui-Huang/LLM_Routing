import math
import itertools

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def get_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a matrix of distances between each pair of cities
num_cities = len(cities)
distance_matrix = [[get_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Function for calculating total tour cost
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Simple greedy / nearest neighbor heuristics to generate an initial feasible tour
def initial_tour(start=0):
    remaining = set(cities.keys())
    tour = [start]
    remaining.remove(start)
    current_city = start

    while remaining:
        next_city = min(remaining, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_c, next_city)
        remaining.remove(next_city)
        current_city = next_city

    tour.append(start)  # return to the depot city
    return tour

# Initialize using the greedy tour
tour = initial_tour()
initial_cost = calculate_tour_cost(tour)

# Now applying our modified Lin-Kernighan Algorithm, we target simple 2-opt swaps to improve the tour
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges, and their reversal won't produce a new tour
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]  # reverse the segment between i and j
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break
    return tour

# Improve the initial tour
optimized_tour = optimize_tour(tour.copy())
optimized_cost = calculate_tour_cost(optimized_tour)

# Print the optimal tour and its total cost
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost}")