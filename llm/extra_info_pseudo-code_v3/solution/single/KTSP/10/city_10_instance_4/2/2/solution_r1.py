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
    chosen_cities = [0]
    remaining_cities = set(V) - {0}
    while len(chosen_cities) < k:
        new_city = random.choice(list(remaining_cities))
        remaining_cities.remove(new_city)
        chosen_cities.append(new_city)
    chosen_cities.append(0)  # return to the depot city
    return chosen_cities

# Calculate the total distance of the tour
def fitness(solution):
    return sum(distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))

# Shaking: swapping two cities randomly (except the depot)
def shake(solution):
    candidate = solution[1:-1]  # exclude the depot
    i, j = random.sample(range(len(candidate)), 2)
    candidate[i], candidate[j] = candidate[j], candidate[i]
    return [0] + candidate + [0]  # include the depot back

# Local search: try all pairs of swaps within the tour to find an improved solution
def local_search(solution):
    best_solution = solution[:]
    best_cost = fitness(solution)

    for i in range(1, len(solution) - 2):  # exclude the depot and last city index
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = fitness(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost

    return best_solution

# Main GVNS algorithm implementation
def gvns(cities, max_iterations, k):
    V = list(cities.keys())
    best_solution = generate_initial_solution(V, k)
    best_fitness = fitness(best_solution)

    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_fitness = fitness(current_improved_solution)

        if current_fitness < best_fitness:
            best_solution = current_solution[:]
            best_fitness = current_fitness

    return best_solution, best_fitness

# Solve the problem
max_iterations = 100
k = 8  # Number of cities including the depot
best_tour, best_cost = gvns(cities, max_iterations, k)

# Print the outputs
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")