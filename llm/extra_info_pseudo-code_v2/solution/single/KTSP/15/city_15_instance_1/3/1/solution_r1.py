import math
import random

# Define the cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def generate_initial_solution():
    k = 6
    city_indices = list(range(1, 15))
    S = [0]  # Start at the depot
    selected_cities = random.sample(city_to indices, k - 1)
    S += selected_cities
    S.append(0)  # Return to the depot
    return S

def shake(S, p):
    i, j = random.sample(range(1, len(S) - 1), 2)
    S[i], S[j] = S[j], S[i]
    return S.copy()

def local_search(S, p):
    best_cost = total_tour_cost(S)
    best_S = S.copy()
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 1):
            for j in range(i + 1, len(S) - 1):
                S_new = S.copy()
                S_new[i], S_new[j] = S_new[j], S_new[i]
                new_cost = total_tour_cost(S_new)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_S = S_new.copy()
                    improved = True
    return best_S

def GVNS():
    itermax = 100
    pmax = 2
    current_solution = generate_initial_solution()
    best_solution = current_solution
    best_cost = total_tour_cost(best_solution)
    
    for _ in range(itermax):
        p = 1
        while p <= pmax:
            S_prime = shake(current_solution, p)
            S_double_prime = local_search(S_prime, p)
            current_cost = total_tour_cost(S_double_prime)
            if current_cost < best_cost:
                best_solution = S_double_prime
                best_cost = current_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Run the GVNS algorithm
final_solution, final_cost = GVNS()
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost:.2f}")