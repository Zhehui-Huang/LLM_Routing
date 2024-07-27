import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities):
    # Initial solution: start at the depot, choose 4 additional cities randomly, and return to the depot
    tour = [0] + random.sample(cities[1:], 4) + [0]
    return tour

def shake(solution, distance_matrix):
    best_cost = calculate_total_distance(solution, distance_error_matrix)
    best_solution = solution[:]
    # Perform 10 random swaps and keep the best shake
    for _ in range(10):
        candidate_solution = solution[:]
        i = random.randint(1, 4)
        j = random.randint(1, 4)
        candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
        cost = calculate_total_distance(candidate_solution, distance_matrix)
        if cost < best_cost:
            best_cost = cost
            best_solution = candidate_solution[:]
    return best_solution

def two_opt(solution, distance_matrix):
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                if i == 0 and j == len(solution) - 1:
                    continue
                new_route = solution[:]
                new_route[i:j] = reversed(solution[i:j])
                if calculate_total_distance(new_route, distance_matrix) < calculate_total_distance(best, distance_matrix):
                    best = new_route
                    improved = True
    return best

def gvns(cities, distance_matrix, nrst):
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_total_distance(best_solution, distance_matrix)

    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        current_solution = two_opt(current_solution, distance_matrix)
        for _ in range(10):  # Shaking iterations
            sp = shake(current_solution, distance_matrix)
            sp = two_opt(sp, distance_matrix)
            sp_cost = calculate_total_distance(sp, distance_matrix)
            if sp_cost < best_cost:
                best_solution = sp
                best_cost = sp_t_cost
    
    return best_solution, best_cost

# Define the cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 90)]

# Prepare distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Run the GVNS algorithm
nrst = 1000  # Number of total restarts in GVNS
best_tour, best_tour_cost = gvns(cities, distance_matrix, nrst)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)