import math
import random

# Coordinates for cities including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Total distance for a given tour
def calculate_total_distance(tour, coordinates):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_dist

# Generate initial random solution
def generate_initial_solution(num_cities, total_cities=15):
    cities = list(range(1, total_cities))
    random.shuffle(cities)
    selected_cities = cities[:num_cities-1]
    selected_cities.insert(0, 0)  # Include depot city as the first city
    selected_cities.append(0)  # Return to depot
    return selected_cities

# Shake the solution - Neighbor solution by swapping two cities
def shake(solution):
    city_idx1, city_idx2 = random.sample(range(1, len(solution) - 1), 2)  # Excluding depot
    solution[city_idx1], solution[city_idx2] = solution[city_idx2], solution[city_idx1]
    return solution

# Variable Neighborhood Descent with two neighborhood structures
def vnd(solution, coordinates):
    best_solution = solution
    best_distance = calculate_total_distance(solution, coordinates)
    
    improved = True
    while improved:
        improved = False
        # Perform swaps (N1)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution, coordinates)
                if new_distance < best_distance:
                    best_solution, best_distance = new_solution, new_distance
                    improved = True
    
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(num_cities, num_restarts=10):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution(num_cities)
        current_solution = vnd(current_solution, coordinates)
        current_cost = calculate_total_distance(current_solution, coordinates)
        
        for _ in range(100):  # Number of iterations per restart
            shaken_solution = shake(current_solution[:])
            improved_solution = vnd(shaken_solution, coordinates)
            improved_cost = calculate_total_distance(improved_solution, coordinates)
            
            if improved_cost < current_cost:
                current_solution, current_cost = improved_solution, improved; &___TCCcFHvZ#0.043883661581265465#7wOGG35 진우고함ꆿ:�#�ed_cost
                break
        
        if current_cost < best_cost:
            best_tour, best_step_cost = current_solution, current_cost
    
    return best_tour, best 

num_cities_to_visit = 12
tour, total_cost = gvns(num_cities_to_visit)
print("Tour:", tour)
print("Total travel cost:", total_cost)