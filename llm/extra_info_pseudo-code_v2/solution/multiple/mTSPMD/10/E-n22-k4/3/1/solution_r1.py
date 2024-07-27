import numpy as np
import random

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

n_cities = len(coordinates)

# Parameters for ACO
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.5

# Robots and depots
robot_depot_mapping = {0: 0, 1: 1, 2: 2, 3: 3}
n_robots = len(robot_depot_mapping)

# Compute Euclidean distance
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Matrix of distances
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]

# ACO algorithm
def aco_tsp():
    best_solution = None
    global_best_cost = float('inf')
    
    pheromone = np.full((n_cities, n_cities), inittrail)
    
    for _ in range(cyclenum):
        all_solutions = []
        all_costs = []
        
        for _ in range(antnum):
            robots_solutions = {r: [robot_depot_mapping[r]] for r in robot_depot_mapping}
            remaining_cities = set(range(n_cities)) - set(robot_depot_mapping.values())
            
            for r in robots_solutions:
                current_city = robots_solutions[r][-1]
                
                while remaining_cities:
                    next_city = select_next_city(current_city, remaining_cities, pheromone, distances, alpha, beta)
                    robots_solutions[r].append(next_city)
                    current_city = next_city
                    remaining_cities.remove(next_city)
                
                robots_solutions[r].append(robot_depot_mapping[r])  # return to its depot
                
            total_tour_cost = calculate_total_cost(robots_solutions, distances)
            all_solutions.append(robots_solutions)
            all_costs.append(total_tour_cost)
        
        # Pheromone update
        pheromone *= (1 - rho)
        for solution, cost in zip(all_solutions, all_costs):
            for r in solution:
                for i in range(len(solution[r]) - 1):
                    pheromone[solution[r][i]][solution[r][i+1]] += 1.0 / cost
        
        # Get the best solution of this generation
        current_min_index = np.argmin(all_costs)
        current_min_cost = all_costs[current_min_index]
        
        if current_min_cost < global_best_cost:
            global_best_cost = current_min_cost
            best_solution = all_solutions[current_min_index]

    return best_solution, global_best_cost

def select_next_city(current_city, remaining_cities, pheromone, distances, alpha, beta):
    probabilities = []
    sum_probabilities = 0
    for city in remaining_cities:
        tau = pheromone[current_city][city]
        eta = 1 / distances[current_city][city] if distances[current_city][city] != 0 else 0
        probability = (tau ** alpha) * (eta ** beta)
        probabilities.append(probability)
        sum_probabilities += probability
    
    probabilities = [p / sum_probabilities for p in probabilities]
    next_city = np.random.choice(list(remaining_cities), p=probabilities)
    return next_city

def calculate_total_cost(solutions, distances):
    total_cost = 0
    for r in solutions:
        tour_cost = sum(distances[solutions[r][i]][solutions[r][i+1]] for i in range(len(solutions[r]) - 1))
        total_cost += tour_cost
    return total_cost

# Execute the ACO
best_solution, best_cost = aco_tsp()

# Output the results
for r in best_solution:
    tour = best_solution[r]
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")
    
print(f"Overall Total Travel Cost: {best_cost:.2f}")