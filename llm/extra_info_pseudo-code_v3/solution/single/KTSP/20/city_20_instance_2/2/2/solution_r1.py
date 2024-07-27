import random
from math import sqrt

# City coordinates including the depot
coordinates = [
    (3, 26),  # Depot
    (85, 74),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

def euclidean_distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

def evaluate_tour(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    cities_to_visit = random.sample(range(1, len(coordinates)), 9)  # 9 random cities + depot
    tour = [0] + cities_to_visit + [0]
    return tour

def shake_solution(tour, k):
    """ Randomly swaps k pairs of cities in the tour """
    new_tour = tour[:]
    for _ in range(k):
        a, b = random.sample(range(1, len(tour)-1), 2)
        new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return new_tour

def variable_neighborhood_search(tour, max_iter=100, k_max=5):
    best_tour = tour[:]
    best_distance = evaluate_tour(best_tour)
    for iteration in range(max_iter):
        k = 1
        while k <= k_max:
            new_tour = shake_solution(best_tour, k)
            new_dist = evaluate_tour(new_tour)
            if new_dist < best_distance:
                best_tour, best_distance = new_tour, new_dist
                k = 1  # Reset k to 1 if improvement found
            else:
                k += 1
    return best_tour, best_distance

def solve_k_tsp():
    initial_tour = generate_initial_solution()
    best_tour, best_distance = variable_neighborhood_search(initial_tour)
    return best_tour, best_distance

# Running the solver
tour, cost = solve_k_tsp()
print("Tour:", tour)
print("Total travel cost:", cost)