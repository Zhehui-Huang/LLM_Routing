import numpy as np
import random

# Define the locations of cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_dist(city_a, city_b):
    return np.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_dist(tour[i], tour[i+1])
    return cost

def generate_initial_solution():
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], 6)
    return chosen_cities

# Local Search Improvement - Simple swap within the tour to improve the current sequence
def local_search(tour):
    min_cost = total_tour_cost(tour)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if i != j:
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_tour = new_tour[:]
    return best_tour

# Variable Neighborhood Descent
def vnd(tour):
    improved = True
    while improved:
        new_tour = local_search(tour)
        if total_tour_cost(new_tour) < total_tour_cost(tour):
            tour = new_tour
        else:
            improved = False
    return tour

# Main GVNS Algorithm
def gvns(k_max=10):
    current_tour = generate_initial_solution() + [0]
    best_tour = current_tour[:]
    best_cost = total_tour_cost(current_tour)
    
    for k in range(1, k_max):
        # Shaking Phase: Randomly change some cities in the tour
        current_tour = generate_initial_solution() + [0]
        # Apply VND
        current_tour = vnd(current_tour)
        current_cost = total_tour_cost(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

    return best_tour, best_cost

# Running the GVNS Algorithm
best_tour, best_cost = gvns()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")