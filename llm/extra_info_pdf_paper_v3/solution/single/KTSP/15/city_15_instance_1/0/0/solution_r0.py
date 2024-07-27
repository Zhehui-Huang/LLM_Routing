import math
import random
from itertools import permutations

# Given city coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Helper function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate all permutations of k-1 cities, excluding the depot, and calculate the tours
def find_best_tour(k):
    best_tour = None
    best_cost = float('inf')
    
    for subset in permutations(range(1, 15), k-1):
        current_tour = [0] + list(subset) + [0]
        cost = total_tour_cost(current_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Run the algorithm for a 6-city tour including the depot
best_tour, best_cost = find_best_tour(6)

# Output result
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))