import numpy as np
import random
from itertools import permutations

# Define the cities coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    """ Calculate total tour cost """
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """ Generate a random initial solution """
    solution = [0]  # start at the depot city
    remaining_cities = list(range(1, len(cities)))
    while len(solution) < 7:
        next_city = random.choice(remaining_cities)
        remaining_cities.remove(next_city)
        solution.append(next_city)
    solution.append(0)  # return to the depot city
    return solution

def local_search(solution, neighborhood_structure):
    """ Perform local search on the given solution """
    if neighborhood_structure == 1:  # N1
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_tour_cost(new_solution) < calculate_tour_cost(solution):
                    return new_solution
    return solution

def shake(solution, p):
    """ Shake the solution in the p-th neighborhood """
    if p == 1:  # Simple shake: swap two random cities
        idx1, idx2 = random.sample(range(1, 6), 2)  # select two indices, excluding the depot
        new_solution = solution[:]
        new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
        return new_solution
    return solution

def gvns(k=7):
    """ Implement the GVNS algorithm """
    itermax = 100
    pmax = 2
    iter = 0
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)

    while iter < itermax:
        current_solution = generate_initial_solution()
        p = 1
        while p <= pmax:
            new_solution = shake(current_solution, p)
            new_solution = local_search(new_solution, p)
            new_cost = calculate_tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1
            else:
                p += 1
        iter += 1
    
    return best_solution, best_wcost

# Run the GVNS algorithm
best_tour, best_total_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)