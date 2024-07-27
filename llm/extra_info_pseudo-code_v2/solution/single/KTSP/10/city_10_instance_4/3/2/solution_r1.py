import math
import random

# City coordinates
cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate Euclidean distance between two cities
def dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Fitness function to calculate total distance of the tour
def fitness(tour):
    return sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial solution by randomly selecting k cities including the depot
def generate_initial_solution(k):
    solution = [0]  # start at the depot city
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    selected_cities = available_cities[:k-1]
    solution.extend(selected_cities)
    solution.append(0)  # end at the depot city
    return solution

# Shake function to create a new nearby solution
def shake(solution, k):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution[:k-1] + [0]

# Local search to explore the neighborhood
def local_search(solution):
    best_solution = solution[:]
    best_fitness = fitness(solution)
    
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_fitness = fitness(new_solution)
            if new_fitness < best_fitness:
                best_solution = new_solution[:]
                best_fitness = new_fitness
    
    return best_solution

# General Variable Neighborhood Search
def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_fitness = fitness(best_solution)
    iter = 0
    
    while iter < itermax:
        p = 1
        while p <= pmax:
            S_prime = shake(best_solution, k)
            S_double_prime = local_search(S_prime)
            if fitness(S_double_prime) < best_fitness:
                best_solution = S_double_prime
                best_fitness = fitness(best_solution)
                p = 1
            else:
                p += 1
        iter += 1
    
    return best_solution, best_fitness

# Parameters
k = 8
itermax = 100
pmax = 5

# Run GVNS
tour, cost = gvns(k, itermax, pmax)
print("Tour:", tour)
print("Total travel cost:", cost)