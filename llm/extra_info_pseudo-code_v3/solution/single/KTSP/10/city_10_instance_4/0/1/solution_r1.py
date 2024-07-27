import numpy as=np
import random
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Construct a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance(i, j)

# Function to evaluate the total travel cost of the tour
def evaluate(tour):
    total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Generate initial solution
def generate_initial_solution():
    cities_list = list(cities.keys())
    cities_list.remove(0)
    selected_cities = random.sample(cities_list, 7)
    tour = [0] + selected_cities + [0]
    return tour

# Shaking function
def shake(solution):
    idx1, idx2 = sorted(random.sample(range(1, len(solution)-1), 2))
    new_solution = solution[:]
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution):
    best_solution = solution[:]
    best_cost = evaluate(solution)
    for i in range(20):  # maximum iterations for VND
        new_solution = shake(best_solution)
        new_cost = evaluate(new_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(restarts):
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    
    for _ in range(restarts):
        initial_solution = generate_initial_solution()
        refined_solution = vnd(initial_solution)
        refined_cost = evaluate(refined_solution)
        
        if refined_cost < best_cost:
            best_solution, best_cost = refined_solution, refined_cost
    
    return best_solution, best_cost

# Execute the algorithm
best_tour, best_total_cost = gvns(50)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total  """
import numpy as np
import random
import math

# Define the coordinates of each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = distance(i, j)
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

# Generate an initial random tour
def generate_initial_tour():
    tour = random.sample(list(cities.keys())[1:], 7)
    tour = [0] + tour + [0]
    return tour

# Calculate the tour cost
def tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Simple swapping of two cities in the tour (excluding the start/end city)
def perform_swap(tour):
    new_tour = tour[:]
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

# Variable Neighborhood Descent
def vnd(best_tour):
    best_cost = tour_cost(best_tour)
    improving = True
    
    while improving:
        improving = False
        new_tour = perform_swap(best_tour)
        cost = tour_cost(new_tour)
        if cost < best_cost:
            best_tour, best_cost = new_tour, cost
            improving = True
    return best_tour

# General Variable Neighborhood Search
def gvns(restarts):
    best_tour = generate_initial_tour()
    best_cost = tour_cost(best_tour)
    
    for _ in range(restarts):
        initial_tour = generate_initial_tour()
        local_best_tour = vnd(initial_tour)
        local_best_cost = tour_cost(local_best_tour)
        
        if local_best_cost < best_cost:
            best_tour, best_cost = local_best_tour, local_best_cost
    return best_tour, best_cost

# Execute the algorithm
best_tour, best_total_cost = gvns(50)

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))