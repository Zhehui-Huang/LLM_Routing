import random
import math
from itertools import permutations

# Step 1: Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Step 2: Define a function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Step 3: Initialize parameters for GVNS
def variable_neighborhood_search(k_cities, max_iters=1000):
    # Step A: Randomly select k cities including the depot
    selected_cities = [0] + random.sample(list(cities.keys())[1:], k_cities - 1)
    best_tour = selected_cities + [0]
    best_cost = calculate_tour_cost(best_tour)
    
    iters = 0
    while iters < max_iters:
        new_tour, new_cost = local_Search(best_tour.copy(), best_cost)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
            iters = 0  # reset iterations since improvement was found
        else:
            iters += 1
    return best_tour, best_cost

def local_Search(tour, current_cost):
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < current_cost:
                return new_tour, new_cost
    return tour, current_cost

def calculate_tour_cost(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return total_cost

# Step 4: Apply GVNS to find a solution
k_cities = 7
tour, total_cost = variable_neighborhood_search(k_cities)

# Print the result
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")