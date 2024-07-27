import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = [
    (54, 87),  # Depot
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Calculate the Euclidean distance matrix for the cities
def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# Function to calculate the total tour distance
def calculate_tour_distance(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    total_cost += distance_matrix[tour[-1]][tour[0]]  # complete the cycle
    return total_cost

# Generate an initial random tour (solution)
def generate_initial_solution(num_cities, k):
    tour = np.random.choice(range(1, num_cities), k-1, replace=False).tolist()
    tour = [0] + tour  # start from the depot city 0
    return tour

# Variables for GVNS
k = 8  # Number of cities to visit including the depot
num_cities = len(cities)
best_solution = generate_initial_solution(num_cities, k)
best_cost = calculate_tour_distance(best_solution, distance_matrix)

# Main GVNS Execution
for _ in range(500):  # Number of iterations
    # Generate new initial solution, shake operation
    new_solution = generate_initial_solution(num_cities, k)
    new_cost = calculate_tour_distance(new_solution, distance_matrix)
    
    # Check if new solution is better
    if new_cost < best_cost:
        best_solution = new_solution
        best_cost = new_cost

    # Swap cities within the new solution, local search (simple 2-opt)
    for i in range(1, len(new_solution)-1):
        for j in range(i+1, len(new_solution)):
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            updated_cost = calculate_tour_distance(new_solution, distance_matrix)
            if updated_cost < best_cost:
                best_cost = updated_cost
                best_solution = new_solution.copy()  # commit this good change
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # revert back

# Closing the tour by returning to the depot
final_tour = best_solution + [0]
final_cost = calculate_tour_distance(final_tour, distance_matrix)

print("Tour:", final_tour)
print("Total travel cost:", final_cost)