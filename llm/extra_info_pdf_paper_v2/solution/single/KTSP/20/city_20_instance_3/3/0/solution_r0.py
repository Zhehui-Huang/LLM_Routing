import math
import random

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate initial random tour starting and ending at the depot
def generate_initial_tour(k):
    tour = random.sample(range(1, len(cities)), k-1)
    tour = [0] + tour + [0]
    return tour

# Calculate the total travel cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Local search to optimize the tour
def local_search(tour):
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if j - i == 1: continue  # Skip if the cities are consecutive
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
        return tour, best_cost

# Variable Neighborhood Search
def variable_neighborhood_search(k, max_iter=100):
    best_tour = generate_initial_tour(k)
    best_cost = tour_cost(best_tour)
    for _ in range(max_iter):
        new_tour = generate_initial_tour(k)
        new_tour, new_cost = local_search(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_test_cost
    return best_tour, best_cost

# Number of cities to visit including the depot
k = 13
best_tour, best_cost = variable_neighborhood_search(k)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)