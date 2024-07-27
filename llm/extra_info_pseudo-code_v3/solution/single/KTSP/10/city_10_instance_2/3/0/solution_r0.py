import random
import math
from itertools import permutations

# Euclidean distance function
def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Fitness calculation (tour length)
def calculate_tour_length(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generation of an initial solution
def generate_initial_solution(cities):
    initial_tour = [0] + random.sample(cities[1:], 5) + [0]
    return initial_tour

# Shake function (using permutations here for simplicity)
def shake(tour):
    middle_section = tour[1:-1]
    random.shuffle(middle_section)
    return [tour[0]] + middle_section + [tour[0]]

# Variable Neighborhood Descent
def vnd(tour, distances):
    best_tour = tour
    best_tour_length = calculate_tour_length(tour, distances)
    improved = True
    
    while improved:
        improved = False
        for perm in permutations(tour[1:-1]):
            new_tour = [tour[0]] + list(perm) + [tour[0]]
            new_tour_length = calculate_tour_length(new_tour, distances)
            if new_tour_length < best_tour_length:
                best_tour = new_tour
                best_tour_length = new_tour_length
                improved = True
                break  # first improvement strategy
    
    return best_tour

# GVNS algorithm
def gvns(cities, distances, Nrst=100):
    S_best = generate_initial_solution(cities)
    best_score = calculate_tour_length(S_best, distances)

    for _ in range(Nrst):
        S = generate_initial_solution(cities)
        while True:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime, distances)
            current_score = calculate_tour_length(S_double_prime, distances)
            if current_score < best_score:
                S_best = S_double_prime
                best_score = current_score
                break

    return S_best

# Main function to setup the problem
def main():
    cities = [
        (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
    ]
    
    # Calculate distances
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = calc_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
    
    # Find the shortest tour
    best_tour = gvns(cities, distances, Nrst=10)
    best_tour_cost = calculate_tour_length(best_tour, distances)
    
    # Results
    return {'Tour': best_tail.rstrip("-"), 'Total travel cost': best_cost}

# Run the program
result = main()
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel cost'])