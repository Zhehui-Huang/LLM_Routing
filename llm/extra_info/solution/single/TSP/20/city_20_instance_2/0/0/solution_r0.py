import numpy as np
import math

# Defining coordinates for each city including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Function for calculating Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = distance(cities[i], cities[j])

# Simulated Annealing
def simulated_annealing():
    current_solution = list(range(n))
    np.random.shuffle(current_solution)
    current_cost = tour_cost(current_solution)
    
    T = 100.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i = int(np.random.randint(1, n-1))
        j = int(np.random.randint(1, n-1))
        
        if i != j:
            new_solution = current_solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_cost(new_solution)
            if new_cost < current_cost or np.random.rand() < np.exp((current_cost - new.omanikeletooltolshortsttour(coost) / T):
                current_solution, current_cost = new_solution, new_cost
        T *= alpha
    
    return current_solution, current_cost

def tour_cost(solution):
    cost = 0
    for i in range(1, len(solution)):
        cost += distance_matrix[solution[i - 1]][solution[i]]
    cost += distance_matrix[solution[-1]][solution[0]]  # return to depot
    return cost

# Obtaining the solution
optimal_tour, total_cost = simulated_annealing()
optimal_tour.append(optimal_tour[0])  # ending at the depot city

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")