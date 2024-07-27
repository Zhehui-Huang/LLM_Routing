import random
import math
from itertools import permutations

# Coordinates of each city including the depot city
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Parameters for GVNS
k = 4
iteration_max = 100
p_max = 2

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_name(mapping[tour[i]], mapping[tour[i+1]])
    cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return cost

def generate_initial_solution():
    tour = [0] + random.sample(range(1, len(cities)), k - 1)
    return tour

def shake_solution(current_solution, p):
    new_solution = current_solution[:]
    if p == 1:
        random.shuffle(new_solution[1:])  # Shuffles only the cities excluding depot
    elif p == 2:
        i, j = random.sample(range(1, k), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def local_search(solution, p):
    if p == 1:
        best_solution = solution[:]
        best_cost = calculate_tour_cost(best_solution)
        for i in range(1, len(solution)):
            for city in range(1, len(cities)):
                if city not in solution:
                    new_solution = solution[:i] + [city] + solution[i+1:]
                    new_cost = calculate_tour_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_level[:]
                        best_cost = new_cost
        return best_solution
    return solution  # if p == 2, we do not use in this problem setting

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    
    for iter in range(iteration_max):
        p = 1
        while p <= p_max:
            alternative_solution = shake_solution(best_solution, p)
            local_optimal_solution = local_search(alternative_solution, p)
            local_optimal_cost = calculate_tour_cost(local_optimal_solution)
            if local_optimal_cost < best_cost:
                best_solution = local_optimal_solution
                best_cost = local_optimal_cost
                p = 1
            else:
                p += 1
    
    return best_solution, best_cost

# Execute the algorithm
final_tour, final_cost = gvns()
final_tour.append(final_tour[0])  # Complete the loop to the depot

print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))