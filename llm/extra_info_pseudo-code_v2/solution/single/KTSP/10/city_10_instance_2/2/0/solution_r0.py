import random
import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial solution: a random tour through 6 cities including depot
def generate_initial_solution():
    remaining_cities = list(cities.keys())
    remaining_cities.remove(0)  # Remove depot from the list
    selected_cities = random.sample(remaining_cities, 5)  # Select 5 more cities randomly
    selected_cities = [0] + selected_cities + [0]  # Include depot as start and end
    return selected_cities

# Calculate the total travel cost for a given tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Functions for neighborhood structures
def shake(tour, k):
    base_city = tour[1:-1]  # Exclude depot
    random.shuffle(base_city)  # Shuffle the cities randomly
    return [0] + base_city + [0]

def local_exchange(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_gvns(tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
    return best_tour

# Variable Neighborhood Descent (VND)
def vnd(tour):
    improved = True
    while improved:
        improved = False
        new_tour = local_exchange(tour)
        new_cost = tour_cost(new_tour)
        current_cost = tour_cost(tour)
        if new_cost < current_cost:
            tour = new_tour[:]
            improved = True
    return tour

# Implementing GVNS
def gvns(k=6, max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = tour_cost(best_tour)
    iter = 0
    while iter < max_iter:
        new_tour = shake(best_tour, 1)
        new_tour = vnd(new_tour)
        new_cost = tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour[:]
            best_cost = new_cost
        iter += 1
    return best_tour, best_cost

# Execute the algorithm
best_tour, best_cost = gvns()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")