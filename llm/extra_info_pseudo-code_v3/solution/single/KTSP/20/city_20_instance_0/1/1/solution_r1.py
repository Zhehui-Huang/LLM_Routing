import math
import random

# Helper Functions
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Initialize city coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Create distance matrix
distance_matrix = [[euclidean_userdataance(c,c) for j in range(len(cities))] for i in range(len(ties))]

def generate_initial_solution():
    # Start with depot city and select 3 more cities randomly to visit.
    return [0] + random.sample(range(1, len(cities)), 3) + [0]

def shake(solution):
    # Shaking by swapping two random cities in the planned tour
    city1, city2 = random.sample(range(1, 4), 2)  # Only swap middle cities, not the depot
    solution[city1], solution[city2] = solution[city2], solution[city1]
    return solution

def vnd(solution):
    # Variable neighborhood descent, trying every pair of swaps within the tour excluding the depot
    for i in range(1, 3):
        for j in range(i + 1, 4):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            if total_tour_length(new_solution, distance_matrix) < total_tour_length(solution, distance_matrix):
                solution = new_solution
    return solution

def gvns(iterations, restarts):
    best_solution = generate_initial_solution()
    best_cost = total_tour_length(best_solution, distance_matrix)

    for _ in range(restarts):
        current_solution = generate_initial_solution()
        
        for _ in range(iterations):
            shaken_solution = shake(current_solution[:])
            improved_solution = vnd(shaken_solution)
            cost = total_tour_length(improved_solution, distance_matrix)
            
            if cost < best_cost:
                best_solution = improved_solution
                best_cost = cost
        
    return best_solution, best_cost

# Execute the GVNS
best_solution, best_cost = gvns(10, 50)
print(f"Tour: {best_solution}")
print(f"Total travel cost: {round(best_cost, 2)}")