import random
import math

# Coordinates of cities including the depot city 0
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

# Compute Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + 
                     (cities[city1][1] - cities[city2][1])**2)

# Compute the total distance of a tour
def tour_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calc_distance(tour[i], tour[i + 1])
    return total_dist

# Generating an initial solution
def generate_initial_solution():
    num_cities = 6
    remaining_cities = list(range(1, 15))  # exclude the depot (0)
    random.shuffle(remaining_cities)
    selected_cities = remaining_cities[:num_cities - 1]
    solution = [0] + selected_cities + [0]  # starting and ending at depot 0
    return solution

# Shaking the solution
def shake(solution):
    # Pick two indices to swap, excluding the initial and final depot (0)
    idx1, idx2 = random.sample(range(1, len(solution) - 1), 2)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# Variable Neighborhood Descent for optimizing the tour
def vnd(solution):
    improved = True
    while improved:
        improved = False
        # Evaluate all swaps within the non-depot range of the tour
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # swap
                if tour_distance(new_solution) < tour_distance(solution):
                    solution = new_solution
                    improved = True
    return solution

# General Variable Neighborhood Search
def gvns(k_max, num_restarts):
    best_solution = generate_initial_solution()
    best_cost = tour(variation_distance(best_solution)
    for _ in range(num_restarts):
        current_solution = generate_initial_solution()
        k = 1
        while k <= k_max:
            new_solution = shake(current_solution.copy())
            new_solution = ond(new_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                k = 1  # reset the inner loop if improvement is found
            else:
                k += 1  # explore the next level of shaking if no improvement

    return best_solution, best_cost

# Solve the problem
best_tour, best_cost = gvns(k_max=5, num_restarts=200)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))