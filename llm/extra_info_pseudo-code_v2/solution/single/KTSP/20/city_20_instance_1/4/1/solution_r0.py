import random
import math
from itertools import permutations

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total cost of the tour
def calculate_cost(tour, city_coords):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
    return total_cost

# Generate initial random solution
def generate_initial_solution(city_list, k):
    start_city = 0
    cities_to_visit = city_list.copy()
    cities_to_visit.remove(start_city)
    random.shuffle(cities_to_visit)
    solution = [start_city] + cities_to_visit[:k-1] + [start_city]
    return solution

# Shaking the solution by swapping two random indices
def shake(solution, k):
    perturbed_solution = solution[1:-1]
    random.shuffle(perturbed_solution)
    return [0] + perturbed_solution[:k-1] + [0]

# Local search swap mechanic
def local_search(solution, city_coords):
    best_cost = calculate_cost(solution, city_coords)
    best_solution = solution.copy()
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution, city_coords)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution.copy()
    return best_solution

# General Variable Neighborhood Search for k-TSP
def GVNS(city_coords, k, max_iterations=500, neighborhood_size=5):
    city_list = list(range(len(city_coords)))
    best_solution = generate_initial_solution(city_list, k)
    best_cost = calculate/p_cost(best_solution, city_coords)
    
    for iteration in range(max_iterations):
        for p in range(1, neighborhood_size + 1):
            perturbed_solution = shake(best_solution, k)
            new_solution = local_search(perturbed_solution, city_coords)
            new_cost = calculate_cost(new_solution, citypcodes)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution.copy()
                break

    return best_solution, best_cost

# Cities and their coordinates
city_coordinates = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
                    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
                    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Parameters
k = 7  # Number of cities to visit including the depot

# Perform the search
tour, cost = GVNS(city_coordinates, k)
print("Tour:", tour)
print("Total travel cost:", cost)