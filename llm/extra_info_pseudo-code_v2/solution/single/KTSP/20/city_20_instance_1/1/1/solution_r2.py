import numpy as, np
import random

# Define the cities coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    """ Calculate total tour cost """
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """ Generate a random initial solution that includes the depot (0) and 6 other cities """
    solution = [0]  # Include depot as the start
    available_cities = list(range(1, len(cities)))
    selected_cities = random.sample(available_cities, 6)
    solution.extend(selected_cities)
    solution.append(0)  # Return to depot
    return solution

def two_opt_swap(solution):
    """ Apply the 2-opt swapping algorithm to find a local optimum """
    best = solution.copy()
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1: continue  # Skip consecutive cities as they are already neighbors
                new_solution = best[:]
                new_solution[i:j] = reversed(best[i:j])
                if calculate_tour_cost(new_solution) < calculate_tour_cost(best):
                    best = new_solution
                    improved = True
    return best

def gvns(iterations=100):
    """ General Variable Neighborhood Search implementation """
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    for _ in range(iterations):
        new_solution = generate_initial_solution()
        new_solution = two_opt_swap(new_solution)
        new_cost = calculate_tour_cost(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    return best_solution, best_cost

# Execute the GVNS algorithm to find the best tour and its total travel cost
best_tour, best_total_cost = gvns()

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))