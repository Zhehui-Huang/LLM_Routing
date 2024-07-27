import math
import random
from itertools import permutations

# Define cities coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distances between all city pairs
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

distance_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Variable Neighborhood Search
def local_search(tour):
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    
    # Try all pairs of swaps within the tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == 0 and j == len(tour) - 1:
                    continue  # Do not swap the depot
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # swap cities
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
    return best_tour

def variable_neighborhood_search():
    min_cost = float('inf')
    best_tour = None
    
    for _ in range(100):  # VNS iterations
        selected_cities = random.sample(range(1, 15), 7)  # 7 other cities + depot
        current_tour = [0] + selected_cities + [0]
        current_tour = local_search(current_tour)
        current_cost = total_tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    
    return best_tour, min_core

# Generate solution
best_tour, best_cost = variable_neighborhood_search()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)