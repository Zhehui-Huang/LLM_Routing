import random
import math
from itertools import permutations

# City coordinates
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

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Subroutine to generate an initial feasible solution
def generate_initial_solution():
    selected_cities = [0]  # Starting with the depot city
    while len(selected_cities) < 6:
        new_city = random.choice(list(cities.keys()))
        if new_city not in selected_cities:
            selected_cities.append(new_city)
    selected_cities.append(0)  # Ending at the depot city
    return selected_cities

# Subroutine to perform local search
def local_search(tour):
    best_cost = total_tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent cities as they're just reverse of the current tour
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# Main GVNS function
def gvns(k_max=10):
    itermax = 100
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    
    for iteration in range(itermax):
        current_solution = generate_initial_solution()
        for k in range(1, k_max + 1):
            new_solution = local_search(current_solution)
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
                break
    
    return best_solution, best_cost

# Running the GVNS algorithm
best_solution, best_cost = gvns()
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost))