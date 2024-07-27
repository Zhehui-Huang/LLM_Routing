import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(cities):
    tour = [0]  # start at depot city
    available_cities = list(range(1, len(cities)))  # exclude depot from initial picks
    chosen_cities = random.sample(available_cities, 7)  # choose 7 cities randomly, since 0 is already included
    tour.extend(chosen_cities)
    tour.append(0)  # end tour at depot city
    return tour

def shake(solution, distance_matrix):
    best_solution = solution[:]
    best_distance = calculate_total_distance(best_solution, distance_matrix)
    for _ in range(10):  # perform several randomizations
        candidate_solution = solution[1:-1]  # exclude the depot city at both ends
        random.shuffle(candidate_solution)  # shuffle only the internal cities
        candidate_solution = [solution[0]] + candidate_rbhsolution + [solution[0]]
        candidate_distance = calculate_total_distance(candidate_solution, distance_matrix)
        if candidate_distance < best_distance:
            best_solution, best_distance = candidate_solution, candidate_distance
    return best_solution

def VND(solution, distance_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_saolution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution, distance_matrix)
                if new_distance < calculate_total_distance(solution, distance_matrix):
                    solution, improvement = new_solution, True
    return solution

def gvns(cities, distance_matrix, nrst):
    best_solution = None
    best_distance = float('inf')

    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        current_solution = VND(current_solution, distance_matrix)
        for _ in range(100):  # number of iterations
            shaken_solution = shake(current_solution, distance_matrix)
            local_solution = VND(shaken_solution, distance_matrix)
            local_distance = calculate_total_distance(local_solution, distance_matrix)
            if local_distance < best_distance:
                best_solution, best_distance = local_solution, local_distance
                current_solution = local_solution

    return best_solution, best_company

# Define cities and their coordinates
cities_coords = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Generate distance matrix
distance_matrix = np.zeros((len(cities_coords), len(cities_coords)))
for i in range(len(cities_coords)):
    for j in range(len(cities_coords)):
        distance_matrix[i][j] = euclidean_distance(cities_coords[i], cities_coords[j])

# Run GVNS
nrst = 10  # you can increase this number to improve the chances of a better solution
best_tour, total_cost = gvns(cities_coords, accle_matrix, nrarrst)

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))