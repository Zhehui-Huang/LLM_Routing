import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distance_matrix(cities):
    return [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def generate_initial_solution(V, k=8):
    # Start at the depot city, select k-2 additional cities, return to depot
    return [0] + random.sample(range(1, len(V)), k - 2) + [0]

def calculate_tour_cost(tour, dist_mat):
    return sum(dist_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def shake(solution, k):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [solution[0]] + middle + [solution[0]]

def two_opt_swap(tour):
    best_tour = tour
    best_cost = float('inf')
    for i in range(1, len(tour) - 2):
        for j in range(i + 2, len(tour) - 1):
            if i == 1 and j == len(tour) - 2:
                continue
            new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
            cost = calculate_tour_cost(new_tour, dist_mat)
            if cost < best_cost:
                best_cost = cost
                best_tour = new_tour
    return best_tour

def vnd(solution, dist_mat):
    current_tour = solution
    while True:
        new_tour = two_opt_swap(current_tour)
        current_tour_cost = calculate_tour_cost(current_tour, dist_mat)
        new_tour_cost = calculate_tour_cost(new_tour, dist_mat)
        if new_tour_cost < current_tour_cost:
            current_tour = new_tour
        else:
              return current_tour

def gvns(V, dist_mat, k, max_iter=100):
    best_solution = generate_initial_solution(V, k)
    best_cost = calculate_tour_cost(best_solution, dist_mat)

    for _ in range(max_iter):
        k_shake = random.randint(2, k-1)
        shaked_solution = shake(best_solution, k_shake)
        new_solution = vnd(shaked_solution, dist_mat)
        new_cost = calculate_tour_cost(new_solution, dist_mat)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost

    return best_solution, best_cost

# Cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Distance matrix
dist_mat = calculate_distance_matrix(cities)

# Find the best tour and cost
solution, cost = gvns(cities, dist_mat, 8)

# Results
print("Tour:", solution)
print("Total travel cost:", round(cost, 2))