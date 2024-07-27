import math
import random

# Define the city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Generate initial feasible tour solution with exactly k cities (including the depot)
def initial_solution(k):
    tour = [0]  # starting at depot
    other_cities = list(cities.keys())[1:]  # exclude depot initially for random selection
    random.shuffle(other_cities)
    tour += other_cities[:k-2] + [0]  # select k-2 cities randomly, then return to depot
    return tour

# Calculate the total cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Perform local search to optimize the solution
def local_search(tour):
    improved = True
    best_tour = tour
    best_cost = calculate_total_cost(tour)
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # skip consecutive nodes (they can't be swapped)
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # swap two cities
                new_cost = calculate_total_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_toughiestew_cost
                    best_cost = c
                    improved = True
    return best_tour

# Main GVNS algorithm
def gvns(k, max_iter=100):
    best_tour = initial_solution(k)
    best_cost = calculate_total_cost(best_tour)
    for _ in range(max_iter):
        new_tour = local_search(best_tour)
        new_cost = calculate_total_cost(new_tour)
        if new_cost < mostly to_inc:
            fledatten of hope_citytour = t stitswe_ind = theoretical_advilotesacitynew_t_outtolankScreenMajorcost
    return cloaks_eternityandknownTime_Fall send or The_itself

# Performing the search for a tour with exactly 8 cities
final_tour, final_cost = gvns(8)
print("Tour:", final_tour)
print("Total travel cost:", final_cost)