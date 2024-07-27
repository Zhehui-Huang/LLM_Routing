import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(V):
    tour = [0] + random.sample(V[1:], 7) + [0]
    return tour

def shake(tour, V):
    middle = tour[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

def two_opt_swap(tour, distance_matrix):
    best_tour = tour[:]
    best_distance = total_distance(best_tour, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]
                new_distance = total_distance(new_tour, distance_matrix)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
    return best_tour

def vnd(tour, distance_matrix):
    return two_opt_swap(tour, distance_matrix)

def gvns(V, distance_matrix, nrst=100):
    best_tour = generate_initial_solution(V)
    best_distance = total_distance(best_tour, distance_matrix)

    for _ in range(nrst):
        s = generate_initial_solution(V)
        while True:
            s_prime = shake(s, V)
            s_double_prime = vnd(s_prime, distance_matrix)
            if total_distance(s_double_prime, distance_matrix) < total_distance(s, distance_matrix):
                s = s_double_prime
            else:
                break

        if total_distance(s, distance_matrix) < best_distance:
            best_tour = s
            best_distance = total_distance(s, distance_matrix)
    
    return best_tour, best_distance

# Coordinates of the cities
cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), 
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Generate the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

best_tour, best_tour_cost = gvns(list(range(10)), distance_matrix)

print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))