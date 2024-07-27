import math
import random

# City coordinates (Depot city 0 included)
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial solution
def generate_initial_solution():
    selected_cities = [0]  # Start at depot city 0
    available_cities = list(cities.keys())[1:]  # Other cities except the depot
    selected_cities += random.sample(available_cities, 3)
    selected_cities.append(0)  # End at depot city 0
    return selected_cities

# Calculate the total travel cost of a tour
def calculate_total_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += euclidean_distance(cities[solution[i]], cities[solution[i+1]])
    return total_cost

# Shaking the solution: Randomly swap two cities (except depot)
def shake(solution):
    candidate = solution[1:-1]  # exclude depot
    random.shuffle(candidate)
    return [0] + candidate + [0]

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                candidate = solution[:]
                candidate[i], candidate[j] = candidate[j], candidate[i]
                if calculate_total_cost(candidate) < calculate_total_cost(solution):
                    solution = candidate
                    improved = True
    return solution

# General Variable Neighborhood Search
def gvns(num_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution()
        current_cost = calculate_total_cost(current_solution)
        
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_total_cost(new_solution)
            
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
            
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            
    return best_solution, best_cost

# Running the GVNS algorithm
num_restarts = 100
best_tour, best_tour_cost = gvns(num_restarts)

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_compute_cost}")