import random
import math

# Define the coordinates for each city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculates the total cost of a tour
def tour_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += calculate_distance(tour[i], tour[i + 1])
    return total

# Generates an initial random solution of k cities including the depot city
def generate_initial_solution(k):
    solution = [0]  # starting at depot
    cities_to_visit = list(cities.keys())
    cities_to_visit.remove(0) # exclude depot from selection
    solution += random.sample(cities_to_visit, k - 1)
    solution.append(0)  # return to depot
    return solution

# Shakes the current solution by performing swaps
def shake(solution, k):
    intermediate_solution = solution[1:-1]  # Remove depot start and end
    random.shuffle(intermediate_solution)
    return [0] + intermediate_solution + [0]

# Local Search for improving the solution
def local_search(solution):
    best_solution = solution[:]
    best_cost = tour_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_solution

# Variable Neighborhood Search with shaking and local search
def variable_neighborhood_search(k, max_iterations, max_p):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    
    for iteration in range(max_iterations):
        for p in range(max_p):
            new_solution = shake(best_solution, k)
            new_solution = local_search(new_solution)
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
        
    return best_solution, best_cost

# Run the algorithm
k = 16  # Including the depot city
max_iterations = 100
max_p = 3

solution, cost = variable_neighborhood_search(k, max_iterations, max_p)
print(f"Tour: {solution}")
print(f"Total travel cost: {cost:.2f}")