import itertools
import math

# Coordinates of the cities including the depot
cities = [
    (16, 90),  # Depot
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
    (32, 79),
]

# Number of cities to be visited including the depot
k = 10

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairwise distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Greedy nearest neighbor algorithm to initialize a tour
def greedy_tour(start, num_cities):
    unvisited = set(range(1, len(cities)))  # skipping the depot initially
    tour = [0]
    current = 0
    
    while len(tour) < num_cities:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # return to the depot
    return tour

# 2-opt algorithm to improve the tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if distances[tour[i]][tour[j]] + distances[tour[i + 1]][tour[j + 1]] < distances[tour[i]][tour[i + 1]] + distances[tour[j]][tour[j + 1]]:
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    return tour

# Calculate the total cost of the tour
def calculate_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate the initial tour
initial_tour = greedy_tour(0, k)

# Improve the tour with 2-opt
optimized_tour = two_opt(initial_tour)

# Compute the cost of the optimized tour
tour_cost = calculate_cost(optimized_tour)

# Outputting the results
result = {
    "Tour": optimized_tour,
    "Total travel cost": tour_cost
}

result