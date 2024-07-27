import numpy as np
import random
from scipy.spatial import distance

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot information
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Ant Colony Optimization Parameters
antnum = 50
cyclenum = 100
alpha = 1.0
beta = 2.0
rho = 0.5
init_pheromone = 0.1

# Calculate distances and heuristic
N = len(cities)
distances = np.zeros((N, N))
heuristic = np.zeros((N, N))
for i in cities:
    for j in cities:
        if i != j:
            dist = distance.euclidean(cities[i], cities[j])
            distances[i][j] = dist
            heuristic[i][j] = 1 / dist if dist != 0 else 0

# Initialize pheromones
pheromones = np.ones((N, N)) * init_pheromone

# Define the ACO algorithm
def aco_algorithm():
    best_cost = float('inf')
    best_solution = None

    for _ in range(cyclenum):
        solutions = []
        for _ in range(antnum):
            robot_tours = {}
            visited_all = set()
            total_cost = 0
            
            for robot_id, start_city in robots.items():
                path = [start_city]
                visited = {start_city}
                current_city = start_city

                while len(visited) < N:
                    possible_moves = [city for city in cities if city not in visited]
                    move_probabilities = []
                    
                    for city in possible_moves:
                        prob = (pheromones[current_city][city]**alpha) * (heuristic[current_city][city]**beta)
                        move_probabilities.append(prob)

                    move_probabilities /= np.sum(move_probabilities)
                    next_city = random.choices(possible_moves, weights=move_probabilities, k=1)[0]
                    
                    path.append(next_city)
                    visited.add(next_city)
                    current_city = next_city

                path.append(start_city)
                cost = calculate_total_cost(path)
                total_cost += cost
                robot_tours[robot_id] = path
                
            solutions.append((total_cost, robot_tours))
        
        min_cost_solution = min(solutions, key=lambda x: x[0])

        # Pheromone update
        pheromones *= (1 - rho)
        for _, tours in solutions:
            for tour in tours.values():
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += 1.0 / min_cost_solution[0]

        if min_cost_solution[0] < best_cost:
            best_cost = min_cost_solution[0]
            best_solution = min_cost_solution[1]

    return best_solution, best_cost

# Calculate total cost
def calculate_total_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Run the algorithm
best_solution, best_cost = aco_algorithm()
overall_total_cost = 0

# Outputting the results
for robot_id, tour in best_solution.items():
    robot_tour_cost = calculate_total_cost(tour)
    overall_total_cost += robot_tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")