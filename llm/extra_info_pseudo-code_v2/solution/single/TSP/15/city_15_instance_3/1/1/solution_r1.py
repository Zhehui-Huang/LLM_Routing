import numpy as np
import itertools

# List of city coordinates including the depot city (index 0)
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Simple greedy approach loading from nearest city to nearest city from the depot
def greedy_tour(start):
    unvisited = set(range(1, len(cities)))  # Exclude depot initially from unvisited
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: distance(cities[current], cities[x]))
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # Complete the loop back to the depot
    return tour

# Attempt 2-opt swap optimization for the tour provided
def two_opt(tour, max_iterations=1000):
    best_tour = tour[:]
    best_cost = calculate_total_cost(best_tour)
    for _ in range(max_iterations):
        start, end = sorted(np.random.choice(list(range(1, len(cities))), 2, replace=False))
        new_tour = best_tour[:start] + best_tour[start:end+1][::-1] + best_tour[end+1:]
        new_cost = calculate_total_cost(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
    return best_tour

# Calculate total travel cost
def calculate_total_cost(tour):
    return sum(distance(cities[tour[i]], cities[tour[i-1]]) for i in range(1, len(tour)))

initial_tour = greedy_tour(0)
improved_tour = two_opt(initial_tour)

# Calculate total travel cost
total_cost = calculate_total_cost(improved_tour)

print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost:.2f}")