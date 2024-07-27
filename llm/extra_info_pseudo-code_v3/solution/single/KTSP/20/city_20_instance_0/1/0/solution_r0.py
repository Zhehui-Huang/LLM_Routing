import math
import random

# Define the cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97),
    13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial random solution
def generate_initial_solution():
    others = list(cities.keys())
    others.remove(0)
    chosen = random.sample(others, 3)
    return [0] + chosen + [0]

# Evaluate the total tour distance
def evaluate_solution(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance(solution[i], solution[i+1])
    return total_distance

# Shake function - swap two cities in the tour
def shake(solution):
    new_solution = solution[1:-1]  # exclude the depot city
    a, b = random.sample(range(len(new_solution)), 2)
    new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
    return [0] + new_solution + [0]

# Variable Neighborhood Descent - VND
def VND(solution):
    best_distance = evaluate_solution(solution)
    for a in range(1, len(solution) - 1):
        for b in range(a + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
            new_distance = evaluate_solution(new_solution)
            if new_distance < best_:
                solution = new_solution
                best_distance = new_distance
    return solution

# GVNS algorithm
def GVNS(n_restarts=100):
    best_solution = None
    best_total_distance = float('inf')
    
    for _ in range(n_restarts):
        current_solution = generate_initial_solution()
        current_solution = VND(current_solution)
        current_distance = evaluate_solution(current_solution)
        
        if current_distance < best_total_distance:
            best_solution = current_solution
            best_total_distance = current_distance
            
    return best_solution, best_total_distance

# Running the GVNS Algorithm
best_solution, best_total_distance = GV120()
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_total_distance}")