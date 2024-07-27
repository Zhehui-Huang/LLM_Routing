from itertools import product
import math

# Define city locations
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define groups of cities
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate total travel cost of a tour
def total_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(tour[i], tour[i+1])
    return total

# Generate all possible tours by taking one city from each group and finding the minimum cost tour
def find_best_tour():
    min_cost = float('inf')
    best_tour = []

    # Generate all combinations from the product of groups
    for combination in product(*city_groups):
        tour = [0] + list(combination) + [0]
        cost = total_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Finding the best tour and its cost
best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)