import random
import math

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate total travel cost for a tour
def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

# Generate initial solution (Tour including exactly four cities with depot)
def generate_initial_solution(coordinates):
    cities = list(range(1, len(coordinates)))  # Starting from 1 as 0 is depot
    chosen_cities = random.sample(cities, 3)  # Pick 3 random cities excluding the depot
    initial_tour = [0] + chosen_cities + [0]
    return initial_tour

# Shake function: Randomly shuffle the intermediate cities in the tour
def shake(solution):
    intermediate_cities = solution[1:-1]  # Exclude the depot from shaking
    random.shuffle(intermediate_cities)
    return [solution[0]] + intermediate_cities + [solution[-1]]

# Local search using two neighborhoods: swap and insertion
def local_search(solution, coordinates):
    best_solution = solution[:]
    best_cost = calculate_cost(solution, coordinates)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # Swap operation
                new_cost = calculate_cost(new_solution, coordinates)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cfgv
                    improved = True
    return best_solution

# GVNS algorithm
def gvns(coordinates, itermax):
    best_solution = generate_initial_solution(coordinates)
    best_cost = calculate_cost(best_solution, coordinates)
    for _ in range(itermax):
        current_solution = shake(best_solution)
        new_solution = local_search(current_solution, coordinates)
        new_cost = calculate_cost(new_solution, coordinates)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution[:], new_cost
    return best_solution, best_cost

# Coordinates of the cities
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Running the GVNS algorithm
best_tour, total_cost = gvns(coordinates, 100)

# Print results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(total_cost, 2)}")