import numpy as np
from math import sqrt
from random import sample, choice
from itertools import permutations

# City coordinates (index corresponds to city number)
city_coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
                    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
                    (53, 80), (21, 21), (12, 39)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = city_coordinates[city1], city_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialization function to randomly select 12 cities including the depot (city 0)
def initialize_cities():
    cities = list(range(1, 15))  # Exclude the depot city 0
    selected_cities = sample(cities, 11)  # Select 11 random cities
    selected_cities.insert(0, 0)  # Include depot city at the beginning
    return selected_cities

# Local Search function: Swapping cities in and out (excluding depot)
def local_search(tour):
    min_tour = tour[:]
    min_cost = tour_cost(tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour)-1):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost(new_tour)
                if new_cost < min_cost:
                    min_tour = new_tour[:]
                    min_cost = new_cost
                    improved = True
        tour = min_tour[:]
    return min_tour

# Calculate tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# General Variable Neighborhood Search (GVNS)
def gvns(k_max, t_max, init_tour):
    best_tour = init_tour[:]
    best_cost = tour_cost(best_tour)
    t = 0

    while t < t_max:
        k = 1
        while k <= k_max:
            # Get a new neighborhood structure
            new_tour = local_search(best_tour[:])
            new_tour = new_tour[:-1] + [new_tour[0]]  # Ensure returning to the depot
            new_cost = tour_cost(new_tour)

            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
                k = 1  # Reset the neighborhood counter
            else:
                k += 1
        t += 1
    
    return best_tour, best_cost

# Main execution: Setup the problem and apply GVNS
np.random.seed(42)  # For reproducibility

initial_tour = initialize_cities() + [0]  # Close the loop back to the depot
final_tour, final_cost = gvns(k_max=5, t_max=100, init_tour=initial_tour)

print("Tour:", final_tour)
print("Total travel cost:", final_cost)