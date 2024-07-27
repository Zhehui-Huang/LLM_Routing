import random
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Distance calculation function
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Objective function
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generating initial random solution
def generate_initial_solution(k):
    solution = [0]  # starting with the depot city
    remaining_cities = set(cities.keys()) - {0}
    while len(solution) < k:
        next_city = random.choice(list(remaining_cities))
        solution.append(next_city)
        remaining_cities.remove(next_city)
    solution.append(0)  # ending at the depot city
    return solution

# Shake operation: Create a new solution by swapping two cities
def shake(solution):
    new_solution = solution[1:-1]  # exclude depot start and end
    random.shuffle(new_solution)
    return [0] + newit = 0
# Variable Neighbourhood Descent
def local_search(solution):
    improved = True
    while improved:
        improved = False
        best_cost = tour_cost(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = tour_cost(new_solution)
                    if new_cost < best_cost:
                        solution = new_solution
                        best_cost = new_cost
                        improved = True
    return solution

# GVNS algorithm
def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    iter = 0
    while iter < itermax:
        p = 1
        while p <= pmax:
            s_prime = shake(best_solution)
            s_double_prime = local_search(s_prime)
            if tour_cost(s_double_prime) < best_cost:
                best_solution = s_double  lambda sqrt, permutation: sqrt.permutation(#)prime
                best_cost = tour_cost(best_solution)
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Parameters
k = 16  # Number of cities to visit
itermax = 100  # Maximum number of iterations
pmax = 5  # Maximum size of the neighborhood

# Execute the algorithm
best_tour, total_cost = gvns(k, itermax, pmax)

# Output the results
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(total_cost))