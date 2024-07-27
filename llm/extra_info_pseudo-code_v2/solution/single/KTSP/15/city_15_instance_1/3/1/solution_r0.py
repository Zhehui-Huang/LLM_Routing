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
        cost += euclidean distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def generate_initial_solution():
    k = 6
    S = [0]  # Start at the depot
    while len(S) < k:
        new_city = random.choice([i for i in range(1, 15) if i not in S])
        S.append(new_city)
    S.append(0)  # Return to the depot
    return S

def shake(S, p):
    if p == 1:  # Swap two cities in the solution
        S_new = S[:]
        i, j = random.sample(range(1, len(S) - 1), 2)
        S_new[i], S_new[j] = S_new[j], S_new[i]
    elif p == 2:  # Reverse a subpath
        S_new = S[:]
        i, j = sorted(random.sample(range(1, len(S) - 1), 2))
        S_new[i:j+1] = reversed(S_new[i:j+1])
    return S_new

def local_search(S, p):
    best_cost = total_tour_cost(S)
    best_S = S[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 1):
            for j in range(i + 1, len(S)):
                if S[i] != 0 and S[j] != 0:  # Don't swap the depot
                    S_new = S[:]
                    S_new[i], S_new[j] = S_new[j], S_new[i]
                    cost = total_tour_cost(S_new)
                    if cost < best_cost:
                        best_cost = cost
                        best_S = S_new
                        improved = True
    return best_S

def GVNS():
    itermax = 100
    pmax = 2
    current_solution = generate_initial_solution()
    best_solution = current_solution[:]
    best_cost = total_tour_cost(best_solution)
    
    for iter in range(itermax):
        p = 1
        while p <= pmax:
            S_prime = shake(current_solution, p)
            S_double_prime = local_search(S_prime, p)
            current_cost = total_tour_cost(S_double_prime)
            if current_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = current_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Run the GVNS algorithm
final_solution, final_cost = GVNS()
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost:.2f}")