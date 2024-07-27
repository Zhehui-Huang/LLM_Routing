import math
from itertools import permutations

# Given coordinates for the cities
cities = {0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 
          4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70), 
          8: (20, 99), 9: (66, 62)}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initial tour setup using a simple approach (Nearest Neighbor)
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities) - {start}
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # returning to the starting city
    return tour

# Function to calculate the total distance and the maximum leg distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = distance(tour[i], tour[i + 1])
        total_cost += leg_distance
        max_leg_distance = max(max_leg_distance, leg_distance)
    return total_cost, max_leg_distance

# Compute an initial tour
initial_tour = nearest_neighbor_tour(0, cities)

# Attempt to improve the tour by evaluating all possible swaps of two cities
def two_opt(tour):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = reversed(tour[i:j + 1])  # Perform the swap
                if evaluate_tour(new_tour)[1] < evaluate_tour(best_tour)[1]:  # Minimizing the maximum leg dist
                    best_tour = new_tour[:]
                    improved = True
        tour = best_tour
    return tour

# Optimize the tour
optimized_tour = two_opt(initial_tour)

# Calculate final results for the tour
total_cost, max_leg_distance = evaluate_tour(optimized_tour)

# Output
print("Tour:", optimized_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))