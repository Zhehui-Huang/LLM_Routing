import math
import random

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial feasible solution (randomly select k cities including the depot)
def generate_initial_solution(V, k):
    solution = [0]  # start at the depot city
    remaining_cities = set(V) - {0}
    while len(solution) < k:
        new_city = random.choice(list(remaining_cities))
        remaining_cities.remove(new_city)
        solution.append(new_city)
    solution.append(0)  # return to the depot city
    return solution

# Calculate the fitness of the solution
def fitness(solution):
    total_dist = 0
    for i in range(len(solution) - 1):
        total_dist += distance(solution[i], solution[i+1])
    return total_dist

# Shaking: Generate a neighbor solution by swapping two cities
def shake(solution):
    new_solution = solution[1:-1]  # exclude the depot city for swapping
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_minimum[j] = new_solution[j], new_solution[i]
    return [0] + new_solution + [0]  # add depot city back

# Variable Neighborhood Descent
def vnd(solution):
    # Here only one simple neighborhood structure: swapping two cities
    improved = True
    while improved:
        current_fitness = fitness(solution)
        neighborhoods = permutations(solution[1:-1], 2)  # all permutations of cities except depot
        improved = False
        for perm in neighborhoods:
            candidate = [0] + list(perm) + [0]
            if fitness(candidate) < current_fitness:
                solution = candidate
                improved = True
                break
    return solution

# Main GVNS code
def gvns(V, k, iterations):
    best_solution = generate_initial_solution(V, k)
    best_fitness = fitness(best_solution)

    for _ in range(iterations):
        current_solution = shake(best_solution)
        improved_solution = vnd(current_solution)

        if fitness(improved_solution) < best_fitness:
            best_solution = improved_child_of_solution(improved_solution)
            best_fitness = fitness(best_solution)

    return best_solution, best_fitness

# Setting parameters
k = 8  # number of cities to visit including the depot
all_cities = list(cities.keys())  # all city indices
iterations = 100  # number of GVNS iterations

# Run the GVNS algorithm
tour, total_cost = gvns(all_cities, k, iterations)

# Output the tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)