import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot information: each robot starting/ending at corresponding depot
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Configuration for the Ant Colony Optimization
antnum = 50
cyclenum = 300
alpha = 1.0
beta = 2.0
rho = 0.5
init_pheromone = 0.1

# Calculate distances and heuristic (inverse of the distance)
N = len(cities)
distances = np.zeros((N, N))
heuristic = np.zeros((N, N))
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean(cities[i], cities[j])
            distances[i][j] = dist
            heuristic[i][j] = 1 / dist

# Initialize pheromones
pheromones = np.ones((N, N)) * init_pheromone

def calculate_total_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def ant_colony_optimization():
    best_solution = None
    best_cost = float('inf')
    best_robot_tours = {}

    for _ in range(cyclenum):
        all_ants_solutions = []
        for ant in range(antnum):
            robot_tours = {}
            remaining_cities = set(cities.keys())
            total_cost = 0
            
            for robot_id, start_depot in robots.items():
                current_city = start_depot
                tour = [current_city]
                remaining_cities.remove(current_city)

                while remaining_cities:
                    probabilities = []
                    possible_moves = list(remaining_cities)
                    
                    if not possible_moves:
                        break
                    
                    total_p = 0
                    for move in possible_moves:
                        p = (pheromones[current_city][move] ** alpha) * (heuristic[current_city][move] ** beta)
                        probabilities.append(p)
                        total_p += p

                    probabilities = [p / total_p for p in probabilities]
                    
                    next_city = random.choices(possible_moves, weights=probabilities)[0]
                    tour.append(next_city)
                    remaining_cities.remove(next_city)
                    current_city = next_city
                
                tour.append(start_depot)
                cost = calculate_total_cost(tour)
                total_cost += cost
                robot_tours[robot_id] = tour
            
            all_ants_solutions.append((total_cost, robot_tours))
        
        # Update pheromones
        pheromones *= (1 - rho)
        for cost, r_tours in all_ants_solutions:
            for rt in r_tours:
                tour = r_tours[rt]
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i + 1]] += 1 / cost
        
        # Check for best solution
        for cost, r_tours in all_ants_solutions:
            if cost < best_cost:
                best_cost = cost
                best_solution = r_tours
                
    return best_cost, best_solution

best_cost, best_solution = ant_colony_optimization()

# Presenting the result
overall_total_cost = 0
for robot_id in best_solution:
    robot_tour = best_solution[robot_id]
    robot_cost = calculate_total_cost(robot_tour)
    overall_total_cost += robot_cost
    print(f"Robot {robot_id} Tour: {robot_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")