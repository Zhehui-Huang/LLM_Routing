import math
import random

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Cost of visiting a sequence of cities
def path_cost(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Initialization function to generate a feasible route with k cities
def initial_solution(k):
    tour = [0]  # start with the depot
    available_cities = list(range(1, len(cities)))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # return to depot
    return tour

# Local search using 2-opt algorithm
def local_search_2opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip consecutive cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if path_cost(new_tour) < path_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# General Variable Neighborhood Search (GVNS)
def GVNS(k, max_iterations):
    best_tour = initial_solution(k)
    best_cost = path_total_cost(best_tour)

    for _ in range(max_iterations):
        new_tour = initial_solution(k)
        new_tour = local_search_2opt(new_tour)
        new_cost = path_cost(new_tour)

        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost

    return best_tour, best_cost

# Setting for the problem
k = 16  # Number of cities to include in the tour
max_iterations = 1000

# Solve the problem
final_tour, final_cost = GVNS(k, max_iterations)

# Display the result
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")