import numpy as np
import random
import math

# Define the coordinates of each city including depot city
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distance between all pairs of cities and store in a matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to calculate the total tour cost
def total_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Simple 2-opt best improvement
def two_opt(tour):
    min_change = 0
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour)):
            if j - i == 1: continue
            new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
            change = total_tour_cost(new_tour, distance_matrix) - total_tour_cost(tour, distance_matrix)
            if change < min_change:
                best_tour = new_tour
                min_change = change
    if min_change < 0:
        return two_opt(best_tour)
    else:
        return tour

# Generate a random initial tour
initial_tour = list(range(n))
random.shuffle(initial_tour)
initial_tour.append(initial_tour[0]) # Return to the depot

# Applying 2-opt to improve the initial tour
improved_tour = two_opt(initial_tour)

# Output the tour and the total travel cost
tour_cost = total_tour_cost(improved_tour, distance_matrix)
result_tour = improved_tour
print(f"Tour: {result_tour}")
print(f"Total travel cost: {tour_cost}")