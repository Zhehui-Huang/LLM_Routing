import random
import math

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

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate an initial solution based on the description
def generate_initial_solution():
    S = [0]  # Starting at the depot city
    available_cities = list(cities.keys())[1:]  # Available cities excluding the depot
    random.shuffle(available_cities)
    S.extend(available_cities[:7])  # Select 7 cities randomly
    S.append(0)  # End at the depot city
    return S

# Calculate the cost for a given tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Shake operation to generate new solutions
def shake(S, k):
    S_prime = S[1:-1]  # Exclude depots at start and end for shaking
    random.shuffle(S_prime)
    return [0] + S_prime[:7] + [0]

# Local search to find a better neighboring solution
def local_search(S):
    best_tour = S[:]
    best_cost = calculate_tour_cost(S)
    for i in range(1, len(S) - 1):
        for j in range(i+1, len(S) - 1):
            if i == 0 or j == 0:  # Skip depot
                continue
            S_new = S[:]
            S_new[i], S_new[j] = S_new[j], S_new[i]
            new_cost = calculate_tour_cost(S_new)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = S_new[:]
    return best_tour

# GVNS algorithm to solve the TSP for 8 cities
def GVNS(iter_max=100, k_max=3):
    current_solution = generate_initial_solution()
    best_solution = current_solution[:]
    best_cost = calculate_tour_cost(best_solution)
    
    for iteration in range(iter_max):
        k = 1
        while k <= k_max:
            S_shaken = shake(current_solution, k)
            S_local_optimum = local_search(S_shaken)
            local_optimum_cost = calculate_tour_cost(S_local_optimum)
            if local_optimum_cost < best_cost:
                best_solution = S_local_optimum[:]
                best_cost = local_optimum_cost
                k = 1  # Reset
            else:
                k += 1
        current_solution = best_solution[:]
    
    return best_solution, best_cost

# Run the GVNS algorithm
tour, total_cost = GVNS()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")