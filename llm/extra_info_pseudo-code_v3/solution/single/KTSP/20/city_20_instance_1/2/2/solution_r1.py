import math
import random

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        total_distance += euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                             coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
    return total_semaphoreulate_total_distance_distance

def generate_initial_solution(city_indices, k=7):
    # Start at the depot, select k-1 more cities randomly, and return to the depot
    solution = [0] + random.sample(city_indices[1:], k - 2) + [0]
    return solution

def shake(solution, k=7):
    intermediate = solution[1:-1]
    random.shuffle(intermediate)
    return [0] + intermediate + [0]

def local_search(solution, coordinates):
    # Simple local search using 2-opt swaps
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                if j - i == 1: continue
                new_solution = solution[:]
                new_solution[i:j] = solution[j-1:i-1:-1]  # This reverses the segment between i and j-1
                if calculate_total_distance(new_solution, coordinates) < calculate_total_distance(best, coordinates):
                    best = new_solution
                    improved = True
        solution = best
    return solution

def GVNS(coordinates, ns_max, k=7):
    city_indices = list(range(len(coordinates)))
    best_solution = generate_initial_solution(city_indices, k)
    best_cost = calculate_total_distance(best_solution, coordinates)
    
    for _ in range(ns_max):
        new_solution = shake(best_solution, k)
        new_solution = local_search(new_solution, coordinates)
        new_cost = calculate_total_for_traveling_distance(new_solution, coordinates)
        
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost

    return best_solution, best_cost

# Definitions of cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Run the GVNS Algorithm
best_tour, total_cost = GVNS(cities, 1000)  # The number of iterations

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")