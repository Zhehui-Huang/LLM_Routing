import random
import math
from itertools import permutations

# City coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generating the initial solution by randomly choosing a subset of k cities
def generate_initial_solution(k):
    all_cities = list(cities.keys())
    all_cities.remove(0)  # Remove the depot city from the list to add later
    selected_cities = random.sample(all_cities, k-1)  # k-1 because we will re-add the depot city.
    random_city_tour = [0] + selected_cities + [0]  # Start and end at the depot
    return random_city_tour

# Function to perform local search by swapping two cities and check for a better solution
def local_search(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:  # skip consecutive cities as they will be reversed
                    continue
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]  # Reverse part of the tour
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True

    return best_tour

# GVNS for k-TSP
def gvns_k_tsp(k, max_iter=100, pmax=5):
    best_tour = generate_initial_solution(k)
    best_cost = tour_cost(best_tour)
    iter_count = 1
    while iter_count <= max_iter:
        s = generate_initial_solution(k)
        p = 1
        while p <= pmax:
            # Generating new solution by shaking: just regenerate new initial solution this time
            s_prime = generate_initial_solution(k)
            # LocalSearch (VND in simplified)
            s_prime_prime = local_search(s_prime)
            new_cost = tour_cost(s_prime_prime)
            if new_cost < best_cost:
                best_tur = s_prime_prime[:]
                best_cost = new_cost
                p = 1  # restarting local search
            else:
                p += 1
        iter_count += 1

    return best_tour, best_cost

# Set number of cities in the tour (k = 8)
k = 8
best_solution, solution_cost = gvns_k_tsp(k)
print("Tour:", best_solution)
print("Total travel cost:", round(solution_cost, 2))