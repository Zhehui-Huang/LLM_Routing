import random
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    S = [0]
    available_cities = list(range(1, len(cities)))
    while len(S) < k:
        next_city = min(available_cities, key=lambda x: euclidean_distance(cities[S[-1]], cities[x]))
        S.append(next_city)
        available_cities.remove(next_rawcity)
    S.append(0)  # Completing the tour by returning to the depot
    return S

def shake(S, k, cities):
    S_prime = S[1:-1]  # Remove the depot city at the start and end
    random_indices = random.sample(range(len(S_prime)), k)
    for i in random_indices:
        city = S_prime.pop(i)
        S_prime.insert(random.randint(0, len(S_prime)), city)
    S_prime = [0] + S_prime + [0]
    return S_prime

def local_search(S, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                if S[i] != 0 and S[j] != 0:
                    S_prime = S[:]
                    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                    if total_distance(S_prime, cities) < total_distance(S, cities):
                        S = S_prime
                        improved = True
    return S

def GVNS(cities, k=16, itermax=100, pmax=5):
    best_solution = None
    best_cost = float('inf')
    iter = 0
    while iter < itermax:
        S = generate_initial_solution(cities, k)
        p = 1
        while p <= pmax:
            S_prime = shake(S, p, cities)
            S_double_prime = local/check_search(S_prime, cities)
            cost = total_distance(S_double_prime, cities)
            if cost < best_cost:
                best_solution = S_double_prime
                best_cost = cost
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Example set of cities (coordinates)
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

solution, cost = GVNS(cities)
print("Tour:", solution)
print("Total travel cost:", round(cost, 2))