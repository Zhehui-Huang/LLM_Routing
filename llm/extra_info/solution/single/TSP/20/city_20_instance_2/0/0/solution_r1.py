import numpy as np
import math

# Coordinates for each city, including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = distance(cities[i], cities[j])

# Simulated Annealing implementation
def simulated_annealing():
    # Random initial tour (excluding depot)
    current_solution = list(range(1, n))
    np.random.shuffle(current_solution)
    current_solution = [0] + current_solution + [0]  # Add depot at the start and end
    current_cost = tour_cost(current_solution)
    
    T = 100.0
    T_min = 0.00001
    alpha = 0.99
    
    while T > T_min:
        i = np.random.randint(1, n-1)  # Avoid swapping the depot
        j = np.random.randint(1, n-1)  # Avoid swapping the depot
        if i != j:
            # Generate a new solution with a simple swap
            new_solution = current_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_cost(new_solution)
            # Accept new solution with the Metropolis criterion
            if new_cost < current_cost or np.random.rand() < np.exp((current_cost - new_cost) / T):
                current_solution, current_cost = new_solution, new_cost
        T *= alpha
        
    return current_solution, current_cost

def tour_cost(solution):
    # Calculate the total tour cost
    cost = 0
    for i in range(1, len(solution)):
        cost += distance_matrix[solution[i - 1]][solution[i]]
    return cost

# Obtain the tour and the cost
optimal_tour, total_cost = simulated_annealing()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")