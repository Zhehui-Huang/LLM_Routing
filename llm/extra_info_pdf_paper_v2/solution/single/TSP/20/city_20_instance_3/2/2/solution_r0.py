import math
import random

# Coordinates of the cities
cities = [
    (30, 56),  # Depot city 0
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72),
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initial greedy tour based on nearest neighbor heuristic
def greedy_tour(start_city=0):
    unvisited = set(range(1, len(cities)))
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(cities[current_city], cities[x]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start_city)  # Return to the depot city
    return tour

# Calculate total travel cost of the tour
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Improve solution by 2-opt swaps
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 or j != len(tour) - 1:  # Don't disconnect the tour
                    if distance(cities[tour[i - 1]], cities[tour[i]]) + distance(cities[tour[j]], cities[tour[j + 1]]) > \
                       distance(cities[tour[i - 1]], cities[tour[j]]) + distance(cities[tour[i]], cities[tour[j + 1]]):
                        tour[i:j+1] = tour[i:j+1][::-1]
                        improved = True
    return tour

# Solve the TSP
initial_tour = greedy_tour()
improved_tour = two_opt(initial_tour)
total_cost = tour_cost(improved_tour)

# Output results
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost}")