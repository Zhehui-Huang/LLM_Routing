import random
import math

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial random solution
def generate_initial_solution(city_coords, k):
    # The depot city is always included and always at the start and end
    other_cities = list(range(1, len(city_coords)))
    selected_cities = random.sample(other_cities, k - 1)
    return [0] + selected_cities + [0]

# Calculate the total cost of the tour
def calculate_total_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_cost

# Local search using 2-opt swap to improve the solution
def local_search(solution, city_coords):
    best_solution = solution[:]
    best_cost = calculate_total_cost(solution, city_coords)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    # perform 2-opt swap
                    new_solution[i:j + 1] = new_solution[i:j + 1][::-1]
                    new_cost = calculate_total_cost(new_solution, city_coords)
                    if new_cost < best_cost:
                        best_solution, best_cost = new_solution, new_cost
                        improved = True
    return best_solution, best_cost

# Function to shake the solution by swapping two random cities
def shake(solution):
    city1, city2 = random.sample(range(1, len(solution) - 1), 2)  # exclude the first and last (depot)
    solution[city1], solution[city2] = solution[city2], solution[city1]
    return solution

# General Variable Neighborhood Search (GVNS)
def GVNS(city_coords, k, nr_iterations=200):
    best_solution = None
    best_cost = float('inf')

    for _ in range(nr_iterations):
        solution = generate_initial_solution(city_coords, k)
        solution, cost = local_search(solution, city_coords)

        for _ in range(100):  # fixed number for shaking iterations
            shaken_solution = shake(solution[:])
            shaken_solution, shaken_cost = local_search(shaken_solution, city_coords)

            if shaken_cost < cost:
                solution, cost = shaken_solution, shaken_cost

        if cost < best_cost:
            best_solution, best_cost = solution, cost

    return best_solution, best_cost

# Given city coordinates
city_coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
                    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
                    (83, 96), (60, 50), (98, 1)]

# Number of cities to visit including the depot
k = 6

# Execute GVNS to find the best tour
best_tour, total_cost = GVNS(city_coordinates, k)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)