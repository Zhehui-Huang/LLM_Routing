import math
import random

# City coordinates (depot + 14 other cities)
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Helper function for calculating Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((city_coordinates[a][0] - city_coordinates[b][0])**2 +
                     (city_coordinates[a][1] - city_coordinates[b][1])**2)

def calculate_tour_cost(tour):
    cost = 0.0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i - 1], tour[i])
    return cost

def generate_initial_solution(k=6):
    S = [0]  # Start from the depot city
    possible_cities = list(range(1, len(city_coordinates)))
    random.shuffle(possible_cities)
    S += possible_cities[:k-1]  # Add k-1 random cities
    S += [0]  # End at the depot city
    return S

def shake(S, Np):
    S_prime = S[:]
    for _ in range(Np):
        i, j = random.randint(1, len(S) - 2), random.randint(1, len(S) - 2)
        S_prime[i], S_prime[j] = S_prime[j], S_prime[i]  # Swap two cities
    return S_prime

def local_search(S, neighborhood):
    if neighborhood == 1:  # Exchange with an unvisited city
        for i in range(1, len(S) - 1):
            for j in range(1, len(city_coordinates)):
                if j not in S:
                    S_prime = S[:]
                    S_prime[i] = j
                    if calculate_tour_cost(S_prime) < calculate_tour_cost(S):
                        return S_prime
    elif neighborhood == 2:  # Swap two cities in the tour
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                if calculate_tour_cost(S_prime) < calculate_tour_cost(S):
                    return S_prime
    return S

def vnd(S):
    k_max = 2
    improvement = True
    while improvement:
        improvement = False
        for k in range(1, k_max + 1):
            original_cost = calculate_tour_cost(S)
            S_prime = local_search(S, k)
            if calculate_tour_cost(S_prime) < original_cost:
                S = S_prime
                improvement = True
                break
    return S

def gvns(k=6, itermax=100, pmax=2):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_tour_cost(best_solution)
    
    iter = 0
    while iter < itermax:
        S = generate_initial_solution(k)
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = vnd(S_prime)
            current_cost = calculate_tour_cost(S_double_prime)
            if current_cost < best_cost:
                best_solution, best_cost = S_double_prime, current_cost
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Running the GVNS algorithm for k-TSP with k=6
k = 6
tour, total_cost = gvns(k)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")