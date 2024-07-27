import random
import math

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

D = calculate_distance_matrix(cities)

def generate_initial_solution(cities):
    tour = [0] + random.sample(list(cities.keys())[1:], 12)
    return tour

def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    cost += distance_matrix[tour[-1]][tour[0]]  # Return to depot
    return cost

def shake(solution):
    idx = random.sample(range(1, len(solution)), 2)
    solution[idx[0]], solution[idx[1]] = solution[idx[1]], solution[idx[0]]
    return solution

def two_opt_swap(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

def vnd(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for k in range(i + 1, len(solution) - 1):
                new_tour = two_opt_swap(solution, i, k)
                if calculate_tour_cost(new_tour, distance_matrix) < calculate_tour_cost(solution, distance_matrix):
                    solution = new_tour
                    improved = True
                    break
            if improved:
                break
    return solution

def gvns(cities, distance_matrix, n_iterations=100):
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_tour_cost(best_solution, distance_matrix)
    
    for _ in range(n_iterations):
        initial_solution = generate_initial_solution(cities)
        current_solution = initial_solution
        current_cost = calculate_tour_cost(current_solution, distance_matrix)
        
        for _ in range(10):  # Shake and VND cycle
            shaken_solution = shake(current_solution[:])
            improved_solution = vnd(shaken_solution, distance_matrix)
            improved_cost = calculate_tour_cost(improved_solution, distance_matrix)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    best_solution.append(0)  # Return to the depot
    return best_solution, best_cost

# Perform the GVNS
tour, cost = gvns(cities, D, 100)
print("Tour:", tour)
print("Total travel cost:", cost)