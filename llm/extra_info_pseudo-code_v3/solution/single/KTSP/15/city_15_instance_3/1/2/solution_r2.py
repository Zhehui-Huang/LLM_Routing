import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def generate_initial_solution(cities, k=10):
    return [0] + random.sample(range(1, len(cities)), k - 1) + [0]

def shake(tour):
    middle = tour[1:-1]
    random.shuffle(middle)
    return [tour[0]] + middle + [tour[-1]]

def two_opt(tour, distance_matrix):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:
                    new_tour = tour[:]
                    new_tour[i:j+1] = tour[j:i-1:-1]
                    if total_distance(new_tour, distance_matrix) < total_distance(best, distance_matrix):
                        best = new_tour[:]
                        improved = True
    return best

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def gvns(cities, k=10, nrst=100):
    distance_matrix = create_distance_matrix(cities)
    best_tour = generate_initial_solution(cities, k)
    best_cost = total_distance(best_tour, distance_matrix)

    for _ in range(nrst):
        current_tour = generate_initial_solution(cities, k)
        current_tour = two_opt(current_tour, distance_matrix)
        for _ in range(10):  # Perform 10 shaking steps
            new_tour = shake(current_tour)
            new_tour = two_opt(new_tour, distance_matrix)
            new_cost = total_distance(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost

    return best_tour, best_cost

# Define cities
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
          (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 77)]

# Run GVNS
best_tour, best_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))