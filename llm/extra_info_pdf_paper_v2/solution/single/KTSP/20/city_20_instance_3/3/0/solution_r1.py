import math
import random

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial random tour with k cities including the depot
def generate_initial_tour(k):
    tour = random.sample(range(1, len(cities)), k - 1)
    tour = [0] + tour + [0]
    return tour

# Calculate total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Perform local search on the tour for improvements
def local_search(tour):
    best_cost = tour_cost(tour)
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 2, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour, best_cost = new_tour, new_cost
                    improvement = True
    return tour, best_cost

# Variable Neighborhood Search for k-TSP
def variable_neighborhood_search(k, max_iter=100):
    best_tour = generate_initial_tour(k)
    best_cost = tour_cost(best_tour)
    
    for _ in range(max_iter):
        new_tour = generate_initial_tour(k)
        new_tincted_tour, new_cost = local_search(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tincted_tour, new_cost
    
    return best_tour, best_cost

# Configuration
k = 13  # Total cities including the depot to visit
best_tour, best_cost = variable_neighborhood_search(k)
print("Tour:", best_message_tour)
print("Total travel cost:", best_cost)