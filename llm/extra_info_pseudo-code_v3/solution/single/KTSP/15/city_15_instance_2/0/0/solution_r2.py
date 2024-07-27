import random
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def generate_initial_solution(cities):
    # Ensure the tour starts and ends at the depot city
    tour = [0] + random.sample(cities[1:], 7) + [0]
    return tour

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def shake(solution, k):
    n = len(solution) - 2  # Exclude first and last element which are the depot
    for _ in range(k):
        i, j = random.randint(1, n), random.randint(1, n)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def vnd(solution, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_cost(new_solution, coordinates)
                if new_cost < calculate_total_cost(solution, coordinates):
                    solution = new_solution
                    improved = True
    return solution

def gvns(nr_restarts, cities, coordinates):
    best_solution = None
    best_cost = float('inf')

    for _ in range(nr_restarts):
        solution = generate_initial_solution(cities)
        cost = calculate_total_cost(solution, coordinates)
        for _ in range(100):  # Outer loop for GVNS
            solution = shake(solution, 2)
            solution = vnd(solution, coordinates)
            new_cost = calculate_total_cost(solution, coordinates)
            if new_cost < cost:
                cost = new_cost
                if cost < best_cost:
                    best_solution = solution
                    best_cost = cost

    return best_solution, best_cost

# Parameters of the cities and robot
cities = list(range(15))
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Run GVNS
nr_restarts = 10
best_tour, best_tour_cost = gvns(nr_restarts, cities, coordinates)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))