import random
import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
def distance_matrix(cities):
    n = len(cities)
    dist_matrix = {}
    for i in range(n):
        dist_matrix[i] = {}
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

dist_matrix = distance_matrix(cities)

# Generate initial solution
def generate_initial_solution(cities, k):
    return [0] + random.sample(list(cities.keys())[1:], k-1)

# Total travel cost
def total_travel_cost(solution, dist_matrix):
    total_cost = sum(dist_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))
    total_cost += dist_matrix[solution[-1]][solution[0]]  # return to depot
    return total_cost

# Neighborhood structure: Swap
def neighborhood_swap(solution):
    n = len(solution)
    for i in range(1, n):
        for j in range(i + 1, n):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            yield new_solution

# Shaking function
def shake(solution, k):
    n = len(solution)
    for _ in range(k):
        i, j = random.sample(range(1, n), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# Variable Neighborhood Descent
def VND(start_solution, dist_matrix):
    current_solution = start_solution[:]
    current_cost = total_travel_cost(current_solution, dist_matrix)
    improved = True
    
    while improved:
        improved = False
        for new_solution in neighborhood_swap(current_solution):
            new_cost = total_travel_cost(new_solution, dist_matrix)
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
                improved = True
                break
    return current_solution

# GVNS Algorithm
def GVNS(cities, k, max_attempts):
    best_solution = generate_initial_solution(cities, k)
    best_cost = total_travel_cost(best_solution, dist_matrix)
    
    for _ in range(max_attempts):
        current_solution = shake(best_solution, k - 1)
        current_solution = VND(current_solution, dist_matrix)
        current_cost = total_travel_cost(current_solution, dist_matrix)
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    best_solution.append(0)  # complete the cycle by returning to depot
    return best_solution, best_cost

# Setting k and number of attempts for the algorithm
sol, cost = GVNS(cities, 8, 100)

# Displaying the output
print("Tour:", sol)
print("Total travel cost:", round(cost, 2))