import math
from itertools import product
from random import randint, choice, random
from operator import itemgetter

# Coordinates of the cities
cities = {
    0: (84, 67),  # depot
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

# Groups of cities
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def generate_initial_tour():
    tour = [0]  # Start at the depot
    used_groups = set()
    available_cities = list(range(1, 10))  # Exclude depot initially

    # Insert one city per group
    for group_id, group_cities in city_groups.items():
        city = choice(group_cities)
        tour.append(city)
        used_groups.add(group_id)
        for g_city in group_cities:
            try:
                available_cities.remove(g_city)
            except ValueError:
                pass

    tour.append(0)  # End at the depot
    
    return tour

def optimize_tour(tour):
    # Simple optimization - Two-opt
    best_cost = total_tour_cost(tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i+2, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j+1] = tour[i:j+1][::-1]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break
    return tour

def perform_trial():
    initial_tour = generate_initial_tour()
    optimized_tour = optimize_tour(initial_tour)
    return optimized_tour

def find_best_tour_over_trials(num_trials):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(num_trials):
        trial_tour = perform_trial()
        trial_cost = total_tour_cost(trial_tour)
        
        if trial_cost < best_cost:
            best_tour = trial_tour
            best_cost = trial_cost
            
    return best_tour, best_cost

# Perform multiple trials to find the optimal solution
best_tour, best_cost = find_best_tour_over_trials(1000)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")