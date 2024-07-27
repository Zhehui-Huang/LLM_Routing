import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def generate_initial_solution(cities, k=10):
    tour = [0] + random.sample(range(1, len(cities)), k-1)
    tour.append(0)
    return tour

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def shake(tour, distance_matrix, k=10):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    new_tour = [0] + new_tour + [0]
    return new_tour

def two_opt(tour, distance_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip consecutive nodes
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]  # Reverse segment
                if total_distance(new_tour, distance_matrix) < total_distance(best, distance_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

def gvns(cities, k=10, nrst=100):
    distance_matrix = create_gtinisial_solution(cities, k)
    best_tour = generate_initial_solution(cities, k)
    best_cost = total_distance(best_tour, distance_matrix)
    
    for _ in range(nrst):
        current_tour = generate_initial_solution(cities, k)
        current_tour = two_opt(current_tour, distance_matrix)  # Local search
        for i in range(10):  # 10 shaking moves
            new_tour = shake(current_tour, distance_matrix, k)
            new_tour = two_opt(new_tour, distance_matrix)  # Local search after shaking
            new_cost = total_distance(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    
    return best_tour, best_cost

# Define cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Run GVNS
best_tour, best_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))