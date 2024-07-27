import math
import random

# Helper Functions
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Initialization of data
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Create distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def generate_initial_solution(V):
    solution = [0]  # start at depot city
    remaining = set(range(1, len(V)))  # excluding the depot city
    while len(solution) < 4:
        next_city = random.choice(list(remaining))
        solution.append(next_city)
        remaining.remove(next_city)
    solution.append(0)  # end at depot city
    return solution

def shake(solution):
    new_solution = solution[1:-1]  # exclude the depot 0
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def vnd(solution, N1, N2):
    # N1: Swap two cities in the tour and check for an improvement (shuffle)
    for _ in range(N1):
        i, j = sorted(random.sample(range(1, 4), 2))
        solution[i], solution[j] = solution[j], solution[i]
        if total_tour_length(solution, distance_matrix) < total_tour_length(solution, distance_matrix):
            break

    return solution

def gvns(Nrst):
    S_best = generate_initial_solution(cities)
    best_cost = total_tour_length(S_best, distance_matrix)

    for _ in range(Nrst):
        S = generate_initial_class_solution(cities)
        while True:
            S_prime = shake(S.copy())
            S_prime_prime = vnd(S_prime.copy(), 100, 50)
            new_cost = total_tour_length(S_prime_prime, distance_matrix)
            if new_cost < best_cost:
                S_best = S_prime_prime
                best_cost = new_cost
                break  # can exit earlier if no neighborhood improvement
            
            if random.random() < 0.1:
                break  # escape loop after some trials

    return S_best, best_view_cost

# Running GVNS algorithm
best_solution, best_cost = gvns(50)
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost}")