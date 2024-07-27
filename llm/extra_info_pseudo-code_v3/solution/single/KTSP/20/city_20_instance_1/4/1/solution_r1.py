import random
import math

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial solution
def generate_initial_solution(V, k):
    solution = [0]  # Start at depot
    available_cities = list(range(1, len(V)))
    random.shuffle(available_cities)
    solution.extend(available_cities[:k-1])
    solution.append(0)  # Return to depot
    return solution

# Calculate total cost of the tour
def calculate_tour_cost(solution, V):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(V[solution[i]], V[solution[i + 1]])
    return total_cost

# Shaking: Generate a neighbor solution by swapping two cities
def shake(solution, V, k):
    new_solution = solution[:]
    num_swaps = random.randint(1, 3)
    for _ in range(num_swaps):
        a, b = random.sample(range(1, k), 2)
        new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution, V, k):
    improved = True
    while improved:
        improved = False
        current_cost = calculate_tour_cost(solution, V)
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution, V)
                if new_cost < current_cost:
                    solution = new_solution[:]
                    current_cost = new_cost
                    improved = True
    return solution

# GVNS
def gvns(V, k, nrst):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        # Generate initial random tour
        S = generate_initial_solution(V, k)
        # Random restarts and generation of neighbors to avoid local minima
        for _ in range(10):
            S_prime = shake(S, V, k)
            S_double_prime = vnd(S_prime, V, k)
            cost = calculate_tour_cost(S_double_prime, V)
            if cost < best_cost:
                best_solution, best_cost = S_double_prime, cost
                break
            S = S_double_prime
    return best_solution, best_cost

# Define cities coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Run GVNS for k-TSP
k = 7
nrst = 100
best_tour, best_cost = gvns(cities, k, nrst)

# Results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))