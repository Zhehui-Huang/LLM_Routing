import math
import random

# Coordinates of the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculates the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generates an initial solution
def generate_initial_solution():
    S = [0]  # start at the depot city
    remaining_cities = list(range(1, len(cities)))  # exclude depot initially
    random.shuffle(remaining_cities)
    S.extend(remaining_cities[:5])  # select 5 other cities randomly
    S.append(0)  # end at the depot
    return S

# Total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function for shaking the solution
def shake(S, Np):
    candidate = S[1:-1]  # excluding the depot city from shake
    if Np == "N1":
        random.shuffle(candidate)
    elif Np == "N2":
        if len(candidate) >= 2:
            i, j = random.sample(range(len(candidate)), 2)
            candidate[i], candidate[j] = candidate[j], candidate[i]
    return [S[0]] + candidate + [S[-1]]

# Local search strategy
def local_search(S, Np):
    best_cost = tour_cost(S)
    best_solution = S
    if Np == "N1":
        # Exchange operation
        for i in range(1, len(S)-1):
            for j in range(1, len(cities)):
                if j not in S:
                    new_solution = S[:i] + [j] + S[i+1:-1] + [S[-1]]
                    new_cost = tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution
    elif Np == "N2":
        # Swap operation
        for i in range(1, len(S)-1):
            for j in range(i + 1, len(S)-1):
                new_solution = S[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = tour_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
    return best_solution

# Variable Neighborhood Descent
def vnd(S):
    neighborhood_structures = ["N1", "N2"]
    improved = True
    while improved:
        improved = False
        for Np in neighborhood_structures:
            new_S = local_search(S, Np)
            if tour_cost(new_S) < tour_cost(S):
                S = new_S
                improved = True
    return S

# GVNS algorithm
def gvns(max_iter=100, pmax=3):
    S = generate_initial_solution()
    best_S = S
    best_cost = tour needs to start and end at the depot_city`tour_cost(S)
    iter = 0
    while iter < max_iter:
        p = 0
        while p < pmax:
            S_shaken = shake(S, "N1" if p % 2 == 0 else "N2")
            S_improved = vnd(S_shaken)
            if tour_cost(S_improved) < best_cost:
                best_S = S_improved
                best_cost = tour_cost(S_improved)
                p = 0  # reset p if improvement is found
            else:
                p += 1
        iter += 1
    return best_S, best_cost

# Run the GVNS function and print results
best_tour, min_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))