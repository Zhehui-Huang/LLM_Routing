import random
import math

# Define city coordinates
city_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Parameters
num_cities_to_visit = 10

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_cost

def generate_initial_solution():
    S = [0]  # Start at the depot
    available_cities = list(range(1, 15))
    random.shuffle(available_cities)
    S.extend(available_cities[:num_cities_to_visit-1])
    S.append(0)  # Return to depot
    return S

def shake(S, k):
    # Perform two-point swap to generate neighboring solution
    S_prime = S[:]
    i, j = random.sample(range(1, len(S_prime)-2), 2)
    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return S_prime

def local_search(S):
    best_cost = calculate_cost(S)
    best_s = S[:]
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]  # Swap two cities
                cost_prime = calculate_cost(S_prime)
                if cost_prime < best_cost:
                    best_s = S_prime[:]
                    best_cost = cost_prime
                    made_improvement = True
                    break
            if made_improvement:
                break
    return best_s

def gvns(max_iter=100, k_max=3):
    S = generate_initial_solution()
    best_S = S[:]
    best_cost = calculate_cost(S)
    iter = 0
    while iter < max_iter:
        for k in range(1, k_max+1):
            S_prime = shake(S, k)
            S_double_prime = local_search(S_prime)
            cost_double_prime = calculate_cost(S_double_prime)
            if cost_double_prime < best_cost:
                best_cost = cost_double_prime
                best_S = S_double_prime[:]
                break
        iter += 1
    return best_S, best_cost

# Running GVNS to find the best tour
best_tour, best_tour_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")