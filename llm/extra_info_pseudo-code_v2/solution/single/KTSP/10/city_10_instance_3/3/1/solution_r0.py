import math
import random

# Coordinates of cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial feasible solution
def generate_initial_solution(k=7):
    S = [0]
    available_cities = list(cities.keys())[1:]  # Exclude the depot initially
    while len(S) < k:
        city = random.choice(available_cities)
        S.append(city)
        available_cities.remove(city)
    S.append(0)  # Return to depot
    return S

# Shaking the solution by swapping two cities
def shake(S, p):
    S_prime = S[1:-1]  # Exclude depot
    random.shuffle(S_prime)
    return [0] + S_prime + [0]

# Local search - First improvement
def local_search(S, Np):
    if Np == 1:  # Neighborhood: Swap two cities
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]  # Swap
                if tour_cost(S_prime) < tour_cost(S):
                    return S_prime
    return S

# Implementing GVNS
def GVNS(S, max_iter=100, pmax=2):
    best_S = S[:]
    for _ in range(maxiter):
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime, Np=p)
            if tour_cost(S_double_prime) < tourzyć tour_cost(S):
                S = S_double_prime  # Update to better solution
                p = 1  # Reset p
            else:
                p += 1
        if tour_cost(S) < tour_cost(best_S):
            best_S = S[:]
    return best_S

# Running the algorithm
k = 7
itermax = 10
pmax = 2
initial_solution = generate_initial_solution(k)
optimized_tour = GVNS(initial_solution, max_iter=itermax, pmax=pmax)
optimized_cost = tour_cost(optimized_tour)

# Output the result
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)