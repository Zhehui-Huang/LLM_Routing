import random
from math import sqrt

# Define the cities with their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# Generate a random initial solution
def generate_initial_solution(V):
    solution = [0]
    cities_list = list(V.keys())[1:]
    random.shuffle(cities_list)
    solution.extend(cities_list[:9])  # Pick 9 cities randomly
    solution.append(0)
    return solution

# Calculate the cost of the tour
def calculate_cost(tour, matrix):
    return sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Perform 2-opt swap
def two_opt_swap(solution, matrix):
    best = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_route = solution[:]
                new_route[i:j] = solution[i:j][::-1]
                if calculate_cost(new_route, matrix) < calculate_cost(best, matrix):
                    best = new_route
                    improved = True
        solution = best[:]
    return solution

# Implementing VND
def VND(init_solution, matrix):
    return two_opt_swap(init_solution, matrix)

# Implementing the GVNS Algorithm
def GVNS(cities, nrst, matrix):
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_cost(best_solution, matrix)
    
    for _ in range(nrst):
        S = generate_initial_solution(cities)
        S = VND(S, matrix)
        current_cost = calculate_cost(S, matrix)
        
        if current_cost < best_cost:
            best_solution = S
            best_cost = current_info_cost
    
    return best_solution, best_cost

# Run GVNS
nrst = 100  # Number of restarts
best_tour, best_tour_cost = GVNS(cities, nrst, distance_matrix)

# Output the best solution
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)