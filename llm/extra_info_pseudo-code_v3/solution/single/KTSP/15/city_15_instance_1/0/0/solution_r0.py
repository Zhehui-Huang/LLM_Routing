import random
import math
from itertools import permutations

# Define the cities and coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate total travel cost of tour
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    return cost

# GVNS components
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 5) + [0]
    return tour

def shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [solution[0]] + middle + [solution[-1]]

def vnd(solution):
    improved = True
    while improved:
        improved = False
        # Subset Selection (N1)
        for i in range(1, 6):  # Iterate through positions in tour (excluding depot)
            for j in range(1, 15):  # Try different cities
                if j not in solution:
                    new_solution = solution[:]
                    new_solution[i] = j
                    new_solution[-1] = 0  # Ensure the tour ends at the depot
                    if tour_cost(new_solution) < tour_cost(solution):
                        solution = new_solution
                        improved = True
                        break
            if improved: break
    return solution

def gvns():
    Nrst = 100  # Number of restarts
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        current_cost = tour_cost(current_solution)
        
        while True:
            new_solution = shake(current_solution)
            improved_solution = vnd(new_solution)
            improved_cost = tour_cost(improved_solution)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
            else:
                break
            
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Running the GVNS algorithm
best_solution, best_cost = gvns()

# Output the result
print(f"Tour: {best_solution}")
print(f"Total travel cost: {round(best_cost, 2)}")