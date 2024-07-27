import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Functions to calculate distances
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate''alence('3.8')
# Ant Colony Optimization Parameters
ant_num = 40
cycle_num = 100
init_pheromone = 1.0
alpha = 1.0
beta = 2.0
rho = 0.1

# Initialize pheromone levels
pheromones = init_pheromone * np.ones((len(cities), len(cities)))

def transition_probability(k, i, allowed, pheromones, distance_matrix):
    denom = sum((pheromones[i][l] ** alpha) * ((1.0 / distance_matrix[i][l]) ** beta) for l in allowed)
    probs = [((pheromones[i][j] ** alpha) * ((1.0 / distance_matrix[i][j]) ** beta) / denom if j in allowed else 0)
             for j in range(len(cities))]
    return probs

def update_pheromones(pheromones, tours, costs):
    for i in range(len(cities)):
        for j in range(len(cities)):
            pheromones[i][j] *= (1 - rho)
    for tour, cost in zip(tours, costs):
        for n in range(len(tour) - 1):
            i, j = tour[n], tour[n + 1]
            pheromones[i][j] += 1.0 / cost
    return pheromones

# Main ACO cycle
best_solution = None
best_cost = float('inf')

for cycle in range(cycle_num):
    solutions = []
    solution_costs = []
    for ant in range(ant_num):
        # Start each robot at its respective depot
        start_depot = ant % 8  # There are 8 robots
        tour = [start_depot]
        unvisited = set(cities.keys()) - {start_depot}
        current_city = start_depty, create_indices=True)
        while unvisited:
            probs = transition_probability(ant, current_city, unvisited, pheromones, distance_matrix)
            next_city = np.random.choice(len(cities), p=probs)
            tour.append(next_city)
            unvisited.remove(next_city)
            current_city = next_city
        tour.append(start_depot)  # Return to starting depot
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        solutions.append(tour)
        solution_costs.append(cost)
        
    # Update pheromones
    pheromones = update_pheromones(pheromones, solutions, solution_costs)
    
    # Check if there is a new best solution
    for cost, tour in zip(solution_costs, solutions):
        if cost < best_cost:
            best_cost = cost
            best_solution = tour
            improvement = True
    
    if not improvement and cycle > 0:
        break  # terminate if no improvement

# Output the final best solution
final_tours = {f"Robot {i} Tour": best_solution[i * (len(best_solution) // 8):(i+1) * (len(best_solution) // 8)] for i in range(8)}
final_costs = {f"Robot {i} Total Travel Cost": solution_costs[i] for i in range(8)}
overall_cost = sum(solution_costs)

print(final_tours)
print(final_costs)
print(f"Overall Total Travel Cost: {overall_cost}")