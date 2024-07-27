import numpy as np
import math
from scipy.spatial.distance import euclidean

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

def initialize_pheromones(n, tau0):
    return np.full((n, n), tau0)

def calculate_transition_probabilities(pheromone_matrix, distance_matrix, alpha, beta):
    attractiveness = (1 / distance_matrix) ** beta
    return (pheromone_matrix ** alpha) * attractiveness

def update_pheromones(pheromone_matrix, tours, distance_matrix, rho, Q):
    for tour, cost in tours:
        for i in range(len(tour) - 1):
            delta_tau = Q / cost
            pheromone_matrix[tour[i]][tour[i+1]] += delta_tau
            pheromone_matrix[tour[i+1]][tour[i]] += delta_tau
        pheromone_matrix *= (1 - rho)
    return pheromone_matrix

def aco_multi_depot_mTSP(cities, depots, num_ants, iterations, alpha, beta, rho, Q, tau0):
    n = len(cities)
    distance_matrix = create_distance_matrix(cities)
    pheromone_matrix = initialize_pheromones(n, tau0)
    
    best_cost = float('inf')
    best_solution = None
    
    for _ in range(iterations):
        solutions = []
        
        for depot in depots:
            for _ in range(num_ants // len(depots)):
                solution, cost = construct_solution(depot, pheromone_matrix, distance_matrix, alpha, beta)
                solutions.append((solution, cost))
                if cost < best_cost:
                    best_cost = cost
                    best_solution = solution

        pheromone_matrix = update_pheromones(pheromone_matrix, solutions, distance_matrix, rho, Q)
    
    return best_solution, best_cost

def construct_solution(depot, pheromone_matrix, distance_matrix, alpha, beta):
    unvisited = set(range(len(distance_matrix))) - {depot}
    tour = [depot]
    current = depot
    
    while unvisited:
        transition_probabilities = calculate_transition_probabilities(
            pheromone_matrix[current].reshape(-1, 1),
            distance_matrix[current].reshape(-1, 1),
            alpha, beta
        )
        probabilities = [transition_probabilities[i] if i in unvisited else 0 for i in range(len(distance_matrix))]
        probabilities /= np.sum(probabilities)
        next_city = np.random.choice(range(len(distance_matrix)), p=probabilities)
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(depot)  # finish the tour at the starting depot
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return tour, cost

# Example usage with sample data
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_ants = 16
iterations = 100
alpha = 1.0
beta = 5.0
rho = 0.1
Q = 100
tau0 = 0.1

# Running the algorithm
best_solution, best_cost = aco_multi_depot_mTSP(cities, depots, num_ants, iterations, alpha, beta, rho, Q, tau0)
print("Best Solution found:", best_solution)
print("Best Solution Cost:", best_cost)