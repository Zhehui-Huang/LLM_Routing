import math
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two city coordinates"""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_route_cost(route):
    """Sum the travel costs for consecutive cities in a tour"""
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return cost

def simulated_annealing(initial_state, start_depot, temperature=1000, cooling_rate=0.995, end_temperature=0.1):
    """Simulated annealing algorithm to optimize tours for the robots"""
    current_temp = temperature
    current_solution = initial_state[:]
    current_cost = calculate_total_route_cost(current_solution)
    
    best_solution = current_solution[:]
    best_cost = current_cost
    
    while current_temp > end_temperature:
        neighbor = current_solution[:]
        i, j = random.sample(range(1, len(neighbor)), 2)  # Avoid the start depot
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap two cities
        
        neighbor_cost = calculate_total_route_cost(neighbor)
        
        if neighbor_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - neighbor_cost) / current_temp):
            current_solution = neighbor[:]
            current_cost = neighbor_cost
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
        
        current_temp *= cooling_rate
        
    return best_solution, best_cost

# Initialize tours for robots starting from depot
initial_solution = list(range(1, len(cities)))  # Exclude the depot initially
random.shuffle(initial_solution)
initial_solution.insert(0, 0)  # Start from depot city 0

# Optimize the tour using Simulated Annealing
optimized_tour, optimized_cost = simulated_annealing(initial_solution, 0)

print("Robot 0 Tour:", optimized_tour)
print("Robot 0 Total Travel Cost:", optimized_cost)

print("\nOverall Total Travel Cost:", optimized_cost)