import math
import random

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def initialize_pheromone_matrix(num_cities, initial_pheromone):
    return [[initial_pheromone for _ in range(num_cities)] for _ in range(num_cities)]

def softmax(x):
    exp_x = [math.exp(i) for i in x]
    sum_exp_x = sum(exp_x)
    return [i / sum_exp_x for i in exp_x]

def choose_next_city(current_city, coordinates, pheromones, visited, alpha, beta, q0):
    probabilities = []
    cities = list(range(len(coordinates)))
    heuristic = []
    
    for city in cities:
        if city not in visited:
            distance = euclidean_distance(coordinates[current_city], coordinates[city])
            if distance == 0: 
                distance = 1e-6 # avoiding divide by zero
            heuristic.append((1 / distance) ** beta)
            probabilities.append(pheromones[current_city][city] ** alpha * (1 / distance) ** beta)
        else:
            heuristic.append(0)
            probabilities.append(0)
    
    if random.random() < q0 and probabilities:
        # Exploitation: choose the best option
        next_city = probabilities.index(max(probabilities))
    else:
        # Exploration: choose based on a biased random probability distribution
        probabilities = softmax(probabilities)
        next_city = random.choices(cities, weights=probabilities, k=1)[0]
    
    if next_city in visited:
        return None  # in case all cities are visited or no valid next move
    return next_city

def calculate_total_cost(tours, coordinates):
    total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def update_pheromones(pheromones, tours, cost, evaporation_rate):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= (1 - evaporation_rate)
    
    for tour in tours:
        tour_contribution = 1 / cost
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i+1]] += tour_contribution
            pheromones[tour[i+1]][tour[i]] += tour_contribution  # symmetric

# City and robot configurations as given in your initial statement
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
               (62, 63), (63, 69), (45, 35)]

num_robots = 2
num_iterations = 10
num_ants = 5
alpha = 1.0
beta = 2.0
evaporation_rate = 0.1
initial_pheromone = 1.0
q0 = 0.9

tours, total_cost = aco_mTSP(coordinates, num_robots, num_iterations, num_ants, alpha, beta, evaporation_rate, initial_pheromone, q0)
print(f"Best Tours: {tours}")
print(f"Best Total Cost: {total_cost}")