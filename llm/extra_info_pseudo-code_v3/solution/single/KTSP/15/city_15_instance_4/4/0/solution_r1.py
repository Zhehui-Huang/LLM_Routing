import math
import random

# Coordinates for cities including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate the Euclidean distance between two cities using their coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute the total distance of a tour
def calculate_total_distance(tour, coordinates):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_dist

# Generate an initial random solution
def generate_initial_solution(num_cities, total_cities=15):
    cities = list(range(1, total_cities))
    random.shuffle(cities)
    selected_cities = cities[:num_cities-1]
    selected_cities.insert(0, 0)  # Include depot city as the first city
    selected_cities.append(0)  # Return to depot
    return selected_cities

# Swap two cities to create a neighboring solution
def shake(solution):
    new_solution = solution[:]
    city_idx1, city_idx2 = random.sample(range(1, len(solution) - 1), 2)  # Exclude depot from swaps
    new_solution[city_idx1], new_solution[city_idx2] = new_solution[city_idx2], new_solution[city_idx1]
    return new_solution

# Perform Variable Neighborhood Descent
def vnd(solution, coordinates):
    improved = True
    best_solution = solution[:]
    best_distance = calculate_total_distance(solution, coordinates)
    
    while improved:
        improved = False
        # Try swaps within solution to find a better local minima
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution, coordinates)
                if new_distance < best_distance:
                    best_solution, best_distance = new_solution, new_distance
                    improved = True
                    break
            if improved:
                break
    
    return best_solution

# General Variable Neighborhood Search Algorithm
def gvns(num_cities, num_restarts=100):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        initial_solution = generate_initial_solution(num_cities)
        current_solution = vnd(initial_solution, coordinates)
        current_cost = calculate_total_distance(current_solution, coordinates)
        
        for _ in range(50):  # Iterations for shaking and local search
            shaken_solution = shake(current_solution)
            improved_solution = vnd(shaken_solution, coordinates)
            improved_cost = calculate_total_distance(improved_solution, coordinates)

            if improved_cost < current_cost:
                current_solution, current_cost = improved_solution, improved_cost

        # Update the best solution found so far
        if current_cost < best_cost:
            best_tour, best_cost = current_solution, current_cost

    return best_tour, best_cost

# Define the number of cities to visit including depot
num_cities_to_visit = 12
tour, total_cost = gvns(num_cities_to_visit)
print("Tour:", tour)
print("Total travel cost:", total_cost)