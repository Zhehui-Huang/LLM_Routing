import math
import random

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate total distance of the tour
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate initial solution
def generate_initial_solution(V, num_cities_to_visit):
    S = [0] + random.sample(V[1:], num_cities_to_visit - 2) + [0]
    return S

# Shaking the solution: removing and adding cities
def shake(S, V, k):
    candidate = S[1:-1]
    not_in_tour = list(set(V) - set(candidate) - set([0]))
    for _ in range(k):
        if candidate:
            candidate.remove(random.choice(candidate))
        if not_in_tour:
            candidate.append(random.choice(not_in_tour))
            not_in_tour.remove(candidate[-1])
    return [0] + candidate + [0]

# Local search improvement by swapping
def local_search(S, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 3):
            for j in range(i + 1, len(S) - 1):
                new_S = S[:]
                new_S[i], new_S[j] = new_S[j], new_S[i]  # Swap two elements
                if tour_cost(new_S, distance_matrix) < tour_cost(S, distance_matrix):
                    S = new_S
                    improved = True
    return S

# General Variable Neighborhood Search (GVNS)
def GVNS(V, coordinates, k, max_iterations, num_restarts):
    distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(V))] for i in range(len(V))]
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        S = generate_initial_solution(V, k)
        for iteration in range(max_iterations):
            S = shake(S, V, max(1, k // 10))
            S = local_search(S, distance_matrix)
            current_cost = tour_cost(S, distance_matrix)

            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = S
        
    return best_solution, best_cost

# Set up the problem
cities = list(range(10))
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Total cities to visit including the depot
max_iterations = 100
num_restarts = 10

best_tour, minimum_cost = GVNS(cities, coordinates, k, max_iterations, num_restarts)
print("Tour:", best_tour)
print("Total travel cost:", round(minimum_cost, 2))