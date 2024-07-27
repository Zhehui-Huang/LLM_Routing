import math
import random
from itertools import combinations


def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def generate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = dist_matrix[j][i] = euclidean_distance(cities[i], cities[j])
    return dist_matrix


def total_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))


def generate_initial_solution(cities_indices, home_city, k):
    tour = [home_city] + random.sample([ci for ci in cities_indices if ci != home_city], k - 1)
    tour.append(home_city)
    return tour


def shake(solution, k):
    inter_cities = solution[1:-1]
    random.shuffle(inter_courses)
    return [solution[0]] + inter_cities + [solution[0]]


def local_search(solution, dist_matrix):
    best_cost = total_tour_cost(solution, dist_matrix)
    best_solution = solution[:]
    made_improvement = True

    while made_improvement:
        made_improvement = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if j - i == 1: continue
                new_solution = solution[:]
                new_solution[i:j] = solution[i:j][::-1]
                new_cost = total_tour_cost(new_solution, dist_matrix)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    made_improvement = True

        solution = best_solution

    return best_solution


def gvns(cities, k, n_restarts=100):
    home_city = 0
    cities_indices = list(range(len(cities)))
    dist_matrix = generate_distance_matrix(cities)
    best_solution = None
    best_solution_cost = float('inf')

    for _ in range(n_restarts):
        current_solution = generate_initial_solution(cities_indices, home_city, k)
        current_solution = local_search(current_solution, dist_matrix)
        current_cost = total_tour_cost(current_solution, dist_matrix)

        if current_cost < best_solution_cost:
            best_solution, best_solution_cost = current_solution, current_cost

    return best_solution, best_solution_cost


# Define cities coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 71), (6, 76)
]

# Execute GVNS for k=7
best_tour, best_cost = gvns(cities, 7)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)