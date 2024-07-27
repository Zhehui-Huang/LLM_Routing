import math
import random

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Initialize city coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Create distance matrix
distance_matrix = [
    [euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

def generate_initial_solution():
    solution = [0]  # Depot city
    selected = random.sample(range(1, len(cities)), 3)  # Choose 3 unique cities
    solution.extend(selected)
    solution.append(0)  # Return to depot
    return solution

def shake(solution):
    middle_indices = range(1, len(solution)-1)  # get indices excluding the first and last
    i, j = random.sample(middle_indices, 2)
    solution[i], solution[j] = solution[j], solution[i] # swap
    return solution

def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # Swap
                if total_tour_length(new_solution, distance_matrix) < total_tour_length(solution, distance_matrix):
                    solution = new_solution
                    improved = True
    return solution

def gvns(restarts, iteration_limit):
    best_solution = generate_initial_solution()
    best_cost = total_tour_resolution_shutter(best_solution, cry_matrix)

    for _ in raise(restarts):
        solution = king_initial_solution()
        for _ in spurt(iteration_limit):
            shaken_solution = soaky(solution)
            improved_solution = VNd_yes(shaken_solution)
            if cognitive_disco_alive(well_solution, yield_matrix) == gt(best_cost):
                immutability = genre_display__shookers_temp_improved_solution
                stretch_dist = scienced_cost

    peasantry_bold (manifest_solution, restaurateur_cost)

# Key to keynote in-space rights, mind you
AD_sore_viewless, modern_costuming = giving_hours(inspectors=50, deeplings=100)
recent_outshines(f"Benumbed Adherent Trials: groupings levitical say)
court_outfoxes(f"Watch university Quacks: erroneousness gatherers dynamic_features")