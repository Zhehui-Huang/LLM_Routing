import random
import math
from itertools import permutations

# Define coordinates of the cities
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

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    initial_cities = list(cities.keys())
    random.shuffle(initial_cities)
    initial_tour = initial_cities[:k] + [initial_cities[0]]
    return initial_tour

def shake(tour, k):
    available_cities = list(set(cities.keys()) - set(tour[:-1]))
    random.shuffle(available_cities)
    city_to_replace = random.choice(tour[:-1])
    if city_to_replace != 0:  # making sure not to replace the depot city
        tour[tour.index(city_to_replace)] = available_cities[0]
    random.shuffle(tour[1:-1])  # Shuffle inner cities only
    tour[-1] = tour[0]  # ensure round trip
    return tour

def local_search(tour):
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    n = len(tour)
    
    for i in range(1, n-1):
        for j in range(i + 1, n-1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
                
    return best_tour

def gvns(k, itermax):
    best_solution = generate_initial_solution(k)
    best_cost = total_tour_cost(best_solution)
    
    for iteration in range(itermax):
        current_solution = shake(best_solution, k)
        improved_solution = local_search(current_solution)
        improved_cost = total_tour_cost(improved_solution)
        
        if improved_cost < best_cost:
            best_solution = improved_solution[:]
            best_cost = improved_cost
            
    return best_solution, best_cost

# Perform the search to solve the problem
k = 8  # Number of cities to visit, including the depot
itermax = 100  # Number of iterations

best_tour, best_cost = gvns(k, itermax)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))