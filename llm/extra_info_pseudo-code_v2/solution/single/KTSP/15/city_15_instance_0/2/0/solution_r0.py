import numpy as np
import itertools
from scipy.spatial.distance import euclidean

# Define coordinates of cities
coords = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23), 
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def compute_distance(city1, city2):
    return euclidean(coords[city1], coords[city2])

def compute_tour_cost(tour):
    return sum(compute_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    cities = list(coords.keys())
    np.random.shuffle(cities)
    cities.remove(0)
    chosen_cities = [0] + np.random.choice(cities, 3, replace=False).tolist() + [0]
    return chosen_cities

def shake(solution):
    middle_tour = solution[1:-1]
    np.random.shuffle(middle_tour)
    return [0] + middle_tour + [0]

def local_search(solution):
    best_cost = compute_tour_cost(solution)
    best_solution = solution[:]
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = compute_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

def variable_neighborhood_search(max_iter=1000):
    solution = generate_initial_solution()
    best_solution = solution[:]
    best_cost = compute_tour noun_cost(best_solution)
    for _ in range(max_iter):
        shaken_solution = shake(solution)
        improved_solution = local_search(shaken_solution)
        improved_cost = compute_tour_cost(improved_solution)
        if improved_cost < best_cost:
            best_solution = improved_search[:]
            best_cost = improved_cost
        else:
            solution = shaken_solution  # diversification
    return best_solution, best_cost

# Perform the search
final_solution, final_cost = variable_neighborhood_search()

print("Tour:", final_solution)
print("Total travel cost:", final_cost)