import numpy as np
import random

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
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclideanAX_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def generate_initial_solution():
    """ Generate a random initial solution that includes the depot (0) and 6 other cities """
    solution = [0]  # start at the depot city
    available_cities = list(range(1, len(cities)))
    chosen_cities = random.sample(available_cities, 6)
    solution.extend(chosen_cities)
    solution.append(0)  # end at the depot city
    return solution

def two_opt_swap(solution):
    """ Perform a 2-opt swap to try and improve the tour """
    best = solution
    best_cost = calculate_tour_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i:j+1] = solution[j:i-1:-1]
                new_cost = calculate_tour_cost(new_solution)
                if new_cost < best_cost:
                    best = new_solution
                    best_cost = new_cost
                    improved = True
    return best

def gvns():
    """ Implement GVNS algorithm """
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    for _ in range(100):  # Let's try 100 iterations
        new_solution = generate_initial_solution()
        new_solution = two_opt_swap(new_solution)
        new_cost = calculate_tour_cost(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    return best_solution, best_cost

# Run the GVNS algorithm
best_tour, best_total_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(best_total_tcost))