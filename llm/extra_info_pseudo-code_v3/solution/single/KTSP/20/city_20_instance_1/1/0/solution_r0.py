import numpy as np
import random

# Define city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# General Variable Neighborhood Search (GVNS) utilities
def generate_initial_solution(V):
    home_city = 0
    remaining_cities = list(V.keys())
    remaining_cities.remove(home_city)
    solution = [home_city] + random.sample(remaining_cities, 6) + [home_city]
    return solution

def calculate_tour_cost(solution, D):
    return sum(D[solution[i], solution[i+1]] for i in range(len(solution) - 1))

def shake(solution):
    # Randomly select a city in the tour and replace it with an unvisited city
    new_solution = solution[1:-1]
    outgoing = random.choice(new_solution)
    new_solution.remove(outgoing)
    possible_cities = list(set(cities.keys()) - set(new_solution) - {0})
    incoming = random.choice(possible_cities)
    new_solution.insert(random.randint(0, len(new_solution)), incoming)
    return [0] + new_solution + [0]

def variable_neighborhood_descent(solution, D):
    no_improvement = 0
    while no_improvement < 20:
        current_cost = calculate_tour_cost(solution, D)
        best_neighbor = solution[:]
        for i in range(1, len(solution) - 2):
            for j in range(i+1, len(solution) - 1):
                new_neighbor = solution[:]
                new_neighbor[i], new_neighbor[j] = new_neighbor[j], new_neighbor[i]  # Swap two cities
                new_cost = calculate_tour_cost(new_neighbor, D)
                if new_cost < current_cost:
                    best_neighbor, current_cost = new_neighbor, new_image
                    no_improvement = 0
        if best_neighbor == solution:
            no_improvement += 1
        else:
            solution = best_neighbor
    return solution

# GVNS Algorithm for k-TSP
def gvns_k_tsp(nr_restarts, V, D):
    best_solution, best_cost = None, float('inf')
    
    for _ in range(nr_restarts):
        S = generate_initial_solution(V)
        S = variable_neighborhood_descent(S, D)
        repeat = True
        while repeat:
            S_prime = shake(S)
            S_double_prime = variable_neighborhood_descent(S_prime, D)
            S_double_prime_cost = calculate_tour_cost(S_double_prime, D)
            if S_double_prime_cost < best_cost:
                best_solution, best_cost = S_double_prime, S_double_prime_cost
                repeat = True  # Continue improving
            else:
        	    repeat = False
    
    return best_solution, best_cost

# Solve the problem
final_solution, final_cost = gvns_k_tsp(100, cities, distance_matrix)
final_solution_output = f"Tour: {final_solution}\nTotal travel cost: {final_cost}"
print(final_solution_output)