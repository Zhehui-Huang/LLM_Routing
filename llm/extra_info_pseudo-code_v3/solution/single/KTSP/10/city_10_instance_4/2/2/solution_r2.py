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
    solution = [0]  # Including the depot city
    chosen_cities = random.sample(V - {0}, k - 1)
    solution.extend(chosen_cities)
    solution.append(0)  # end at the depot city
    return solution

# Calculate the total distance of the tour
def fitness(solution):
    return sum(distance(solution[i], solution[i + 1]) for i in range(len(solution) - 1))

# Shaking function: swap two random cities
def shake(solution):
    a, b = random.sample(range(1, len(solution) - 1), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

# Variable Neighborhood Descent (VND) - trying different swaps to improve the solution
def variable_neighborhood_descent(solution):
    improved = True
    while improved:
        best_fitness = fitness(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_fitness = fitness(new_solution)
                if new_fitness < best_fitness:
                    solution = new_solution
                    best_fitness = new_fitness
                    improved = True
                    break
            else:
                continue
            break
        else:
            improved = False
    return solution

# General Variable Neighborhood Search
def gvns(V, k, iterations):
    V = set(V)
    best_solution = generate_initial_solution(V, k)
    best_fitness = fitness(best_solution)

    for _ in range(iterations):
        s_prime = shake(best_solution[:])
        s_double_prime = variable_neighborhood_descent(s_prime)
        if fitness(s_double_prime) < best_fitness:
            best_solution = s_double_double_prime
            best_fitness = fitness(best_solution)

    return best_solution, best_fitness

# Execute the algorithm
k = 8  # Include the depot in the city count
all_cities = list(cities.keys())
best_tour, best_cost = gvns(all_cities, k , 100)

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))