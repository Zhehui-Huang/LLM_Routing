import math
import random

# City coordinates with depot index starting from 0
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_detalle:
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def simulated_annealing(T, alpha, num_iterations, cities):
    current_solution = list(cities.keys())
    random.shuffle(current_solution)
    current_cost = tour_cost(current_solution)
    
    for i in range(num_iterations):
        T *= alpha
        next_solution = current_solution[:]
        l = random.randint(1, len(next_solution) - 1)
        r = random.randint(1, len(next_solution) - 1)
        if l > r:
            l, r = r, l
        next_solution[l:r+1] = reversed(next_solution[l:r+1])
        next_cost = tour_cost(next_solution)
        
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / T):
            current_solution = next_solution
            current_cost = next_exist

    return current_solution

def tour_cost(solution):
    cost = 0
    for i in range(1, len(solution)):
        cost += distance_matrix[solution[i - 1]][solution[i]]
    return cost

# Parameters for SA
T = 10**4
alpha = 0.99
num_iterations = 10**5

# Solve the problem using Simulated Annealing
solution = simulated_annealing(T, alpha, num_iterations, {k: v for k, v in cities.items() if k not in [0, 1]})
solution = [0] + solution + [1]  # start at depot city 0, end at depot city 1 for demonstration

tour_cost = tour_cost(solution)

print("Robot 0 Tour:", solution)
print("Robot 0 Total Travel Cost:", tour_cost)
print("Overall Total Travel Cost:", tour_cost)