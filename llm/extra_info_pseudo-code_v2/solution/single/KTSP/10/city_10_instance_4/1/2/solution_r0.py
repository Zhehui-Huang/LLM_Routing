import math
import random

# Define the cities with their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate the total travel cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate an initial solution
def generate_initial_solution(k=8):
    tour = [0]
    available_cities = list(cities.keys())[1:]
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)
    return tour

# Local search operation
def local_search(solution):
    best_solution = solution[:]
    best_cost = total_cost(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 1 and j == len(solution) - 2:
                    continue
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
    return best_solution

# Variable Neighborhood Search
def variable_neighborhood_search(max_iter=100):
    best_solution = generate_initial_solution()
    best_cost = total_prog_list = total_cost(best_solution)
    for _ in range(max_iter):
        new_solution = generate_initial_solution()
        new_solution = local_search(new_solution)
        new_cost = total_cost(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost
    return best_solution, best_cost

# Run the Variable Neighborhood Search to solve the problem
final_tour, final_cost = variable_neighborhood_search()

print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))