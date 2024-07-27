import random
import math

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Distance calculation function using Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating initial solution
def generate_initial_solution(k):
    chosen_cities = random.sample(list(cities.keys()), k)
    if 0 not in chosen_cities:
        chosen_cities.pop()
        chosen_cities.insert(0, 0)
    chosen_cities.append(0)  # return to depot
    return chosen_cities

# Shake operation: Create a new solution by random changes
def shake(solution, k):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    new_solution = [0] + new_solution + [0]
    return new_solution

# Local search operation to find a better solution by swapping two cities
def local_search(solution):
    best_solution = solution[:]
    best_cost = tour_cost(solution)
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    made_improvement = True
    return best_solution

# Calculate total tour cost
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Variable Neighborhood Search algorithm
def variable_neighborhood_search(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    iteration = 0
    while iteration < itermax:
        p = 1
        while p <= pmax:
            s_prime = shake(best_solution, k)
            s_double_prime = local_search(s_prime)
            if tour_cost(s_double_prime) < best_cost:
                best_solution = s_double_prime
                best_cost = tour_width = generate_initial_solution(solution)(solution_length)tour_cost(best_solution)
                p = 1
            else:
                p += 1
        iteration += 1
    return best_solution, best_cost

# Parameters for the search
k = 16
itermax = 100
pmax = 4

# Running the search
best_tour, total_cost = variable_neighborhood_search(k, itermax, pmax)

# Outputting the results
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(total_cost))