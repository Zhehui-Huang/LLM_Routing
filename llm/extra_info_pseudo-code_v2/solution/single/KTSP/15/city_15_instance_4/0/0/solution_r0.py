import random
import math
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution(coordinates, k):
    cities = list(range(1, len(coordinates)))  # exclude the depot which is 0
    random.shuffle(cities)
    solution = [0] + cities[:k-1] + [0]  # start and end at the depot
    solution = sorted(solution[1:-1], key=lambda x: euclidean_distance(coordinates[0], coordinates[x]))
    return [0] + solution + [0]

def shake(solution, swap_count):
    shaken_solution = solution[1:-1]
    for _ in range(swap_count):
        i, j = random.sample(range(len(shaken_solution)), 2)
        shaken_solution[i], shaken_solution[j] = shaken_solution[j], shaken_solution[i]
    return [0] + shaken_solution + [0]

def local_search(solution, coordinates, k):
    best_solution = solution[:]
    best_cost = total_distance(best_solution, coordinates)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, k):
            for j in range(i + 1, k):
                candidate_solution = solution[:]
                candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
                candidate_cost = total_distance(candidate_solution, coordinates)
                if candidate_cost < best_cost:
                    best_solution = candidate_solution[:]
                    best_cost = candidate_cost
                    improved = True
                    
    return best_solution

def gvns(coordinates, k, max_iter=100, pmax=5):
    best_solution = generate_initial_solution(coordinates, k)
    best_cost = total_distance(best_solution, coordinates)

    for _ in range(max_iter):
        for p in range(1, pmax + 1):
            current_solution = shake(best_solution, p)
            current_solution = local_search(current_solution, coordinates, k)
            current_cost = total_distance(current_solution, coordinates)

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

    return best_solution, best_cost

# Coordinates of the cities including the Depot
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Solve the problem for 12 cities including the depot
k = 12
tour, cost = gvns(coordinates, k)
print("Tour:", tour)
print("Total travel cost:", cost)