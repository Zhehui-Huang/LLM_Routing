import random
import math

# Define the coordinates of the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Helper Function: Calculate Euclidean Distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Function: Calculate Total Distance of the Tour
def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function: Generate Initial Solution
def generate_initial_solution():
    # Sample 6 unique cities excluding city 0, add city 0 to the start and end
    sample = random.sample(range(1, 10), 6)
    return [0] + sample + [0]

# Function: Shake (perturbation to solution)
def shake(solution):
    middle_section = solution[1:-1]
    random.shuffle(middle_section)
    return [0] + middle_section + [0]

# Function: Variable Neighborhood Descent
def vnd(solution):
    min_solution = solution[:]
    min_cost = total_distance(min_solution)
    
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            candidate_solution = min_solution[:]
            candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
            candidate_cost = total_distance(candidate_solution)
            if candidate_cost < min_cost:
                min_solution = candidate_solution[:]
                min_cost = candidate_cost
                
    return min_solution

# Function: General Variable Neighborhood Search (GVNS) for k-TSP
def gvns(nrst):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    
    for _ in range(nrst):
        current_solution = generate_initial_init_solution()
        while True:
            shaken_solution = shake(current_solution)
            improved_solution = vnd(shaken_solution)
            improved_cost = total_distance(improved_solution)
            
            if improved_cost < best_cost:
                best_solution = improved_solution[:]
                best_cost = improved_cost
                current_solution = best_solution[:]
            else:
                break
    
    return best_solution, best_cost

# Executing GVNS
nrst = 100  # Number of restart attempts
best_tour, optimal_cost = gvns(nrst)
print("Tour:", best_tour)
print("Total travel cost:", round(optimal_cost, 2))