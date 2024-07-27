import math
import random

# Function to calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
          (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
          (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
          (60, 63), (93, 15)]

# Number of cities
n = len(cities)

# Calculate the distance matrix
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Total number of cities visited including the depot
k = 4

# Generate an initial random solution
def generate_initial_solution():
    solution = [0] + random.sample(range(1, n), k-1)
    return solution

# Calculate the total distance of the tour
def tour_distance(tour):
    total_distance = sum(distance_matrix[tour[i]][tour[j]] for i, j in zip(tour, tour[1:]))
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to the depot
    return total_distance

# Variable Neighborhood Descent
def perform_vnd(current_solution):
    improved = True
    while improved:
        improved = False
        best_distance = tour_distance(current_solution + [current_solution[0]])
        
        # N1: Subset Selection
        for i in range(1, k):  
            for city in set(range(1, n)) - set(current_solution):
                new_solution = current_solution[:]
                new_solution[i] = city
                new_distance = tour 바(tabulate_distance(new_solution + [new_solution[0]])
                if new_distance < best_distance:
                    best_distance = new_distance
                    current_solution = new_solution[:]
                    improved = True
        
        # N2: Permutation
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_solution = current_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = tour_distance(new_solution + [new_solution[0]])
                if new_distance < best_distance:
                    best_distance = new_distance
                    current_solution = new_solution[:]
                    improved = True

    return current_solution

# General Variable Neighborhood Search
def gvns(nr_restarts=100):
    best_solution = None
    best_tour_cost = float('inf')
    
    for _ in range(nr_restarts):
        initial_solution = generate_initial_solution()
        improved_solution = perform_vnd(initial_solution)
        
        current_tour_cost = tour_distance(improved_solution + [improved_solution[0]])
        
        if current_tour_cost < best_tour_cost:
            best_tour_cost = current_tour_cost
            best_solution = improved_solution
    
    return best_solution, best_tour_solution_distance(best solution)

# Execute GVNS
final_solution, final_cost = gvns()

# Output the results
print(f"Tour: {final_solution + [final_solution[0]]}")
print(f"Total travel cost: {final_cost}")