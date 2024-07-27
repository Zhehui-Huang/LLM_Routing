import numpy as np
import random

# City coordinates given
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Distance calculation (Euclidean)
def calc_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generating the distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = calc_distance(cities[i], cities[j])

# Solution fitness function
def tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Generate random initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 4) + [0]
    return tour

# Shaking the solution by swapping two random cities
def shake(solution):
    new_solution = solution[1:-1]
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return [0] + new_solution + [0]

# Local search optimization using variable neighborhood descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if tour_cost(new_solution) < tour_cost(solution):
                        solution = new_solution
                        improved = True
    return solution

def gvns(max_restarts):
    best_solution = generate_initial_solution()
    best_cost = tour_cost(best_solution)
    
    for _ in range(max_restarts):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = tour_cost(new_solution)
            if new_cost < tour_cost(current_solution):
                current_solution = new_solution
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
            else:
                break
    
    return best_solution, best_cost

# Running the GVNS algorithm with a defined number of restarts
best_solution, best_cost = gvns(1000)

# Output the result according to the format requirements
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))