import random
import math
from itertools import permutations

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate total travel cost for a tour
def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

# Generate initial solution (randomly choose four cities including depot)
def generate_initial_solution(cities):
    solution = [0]  # Start at the depot
    available_cities = cities[1:]  # Exclude the depot
    while len(solution) < 4:
        city = random.choice(available_cities)
        available_cities.remove(city)
        solution.append(city)
    solution.append(0)  # Return to depot
    return solution

# Shake function to generate a random neighborhood solution
def shake(current_solution):
    shuffled_solution = current_solution[1:-1]
    random.shuffle(shuffled_solution)
    return [current_solution[0]] + shuffled_solution + [current_solution[0]]

# Local Search using two neighborhoods N1 and N2
def local_search(solution, coordinates):
    best_solution = solution[:]
    best_cost = calculate_cost(solution, coordinates)
    improved = True
    while improved:
        improved = False
        # N1: Swap two cities in the route
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution, coordinates)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    improved = True
    return best_solution

# GVNS algorithm
def gvns(cities, coordinates, itermax):
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_cost(best_solution, coordinates)
    
    for _ in range(itermax):
        current_solution = shake(best_solution)
        new_solution = local_search(current_solution, coordinates)
        new_cost = calculate_cost(new ution, coordinates)
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

cities = list(range(10))  # list of cities by index
best_tour, total_cost = gvns(cities, coordinates, 100)  # Run GVNS with 100 iterations

# Output result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")