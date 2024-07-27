import numpy as np
import random
import math

# Cities and Coordinates with depots included
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8
# All robots start at depot city 0
robots_initial_city = 0

def euclidean_distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Simulated Annealing implementation
def simulated_annealing(init_tour, temp, alpha, num_iterations):
    current_tour = init_tour[:]
    min_tour = current_tour[:]
    min_cost = calculate_total_cost(min_tour)
    
    current_temp = temp
    for _ in range(num_iterations):
        new_tour = generate_new_tour(current_tour)
        new_cost = calculate_total_cost(new_tour)
        current_cost = calculate_total_cost(current_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
            current_tour = new_tour[:]
            if new_cost < min_cost:
                min_cost = new_cost
                min_tour = new_tour[:]
        
        current_temp *= alpha
    
    return min_tour, min_cost

def calculate_total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

def generate_new_tour(tour):
    new_tour = tour[:]
    idx1, idx2 = random.sample(range(1, len(tour)-1), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

# Setup initial tour (selecting random assignments initially, then optimizing)
initial_tour = list(cities.keys())
random.shuffle(initial_tour)
initial_tour = [robots_initial_city] + initial_tour + [robots_initial_city]  # start and end at the depot

# Perform Simulated Annealing
optimized_tour, optimized_cost = simulated_annealing(initial_tour, temp=10000, alpha=0.995, num_iterations=1000)
print("Optimized Tour:", optimized_tour)
print("Optimized Total Travel Cost:", optimized_cost)