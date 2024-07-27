import numpy as np
import random

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1
alpha = 1
beta = 2
rho = 0.1

# City coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
])

def euclidean_distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

num_cities = len(coordinates)
distance_matrix = np.array([[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])
pheromone = np.full((num_cities, num_cities), inittrail)
heuristic = 1 / (distance_matrix + 0.0001)  # Avoid division by zero

def ant_colony_optimization():
    best_costs = [np.inf, np.inf]
    best_solutions = [None, None]
    
    for cycle in range(cyclenum):
        solutions, costs = [], []
        
        for ant in range(antnum):
            if ant % 2 == 0:
                start_depot = 0
            else:
                start_depot = 1
            solution, cost = construct_solution(start_depot)
            solutions.append(solution)
            costs.append(cost)
        
        pheromone *= (1 - rho)
        for i, solution in enumerate(solutions):
            for j in range(len(solution) - 1):
                pheromone[solution[j]][solution[j+1]] += 1 / costs[i]
        
        for i in range(2):  # Since we have two robots
            if costs[i] < best_costs[i]:
                best_costs[i] = costs[i]
                best_solutions[i] = solutions[i]
                print(f"New best cost for robot {i} found: {best_costs[i]}")
        
    return best_solutions, best_costs

def construct_solution(start_depot):
    unvisited = list(range(num_cities))
    unvisited.remove(start_depot)
    current_city = start_depot
    solution = [current_city]
    cost = 0
    
    while unvisited:
        next_city = choose_next_city(current_city, unvisited)
        solution.append(next_city)
        cost += distance_matrix[current_city][next_city]
        unvisited.remove(next_city)
        current_city = next_city
    
    solution.append(start_depot)
    cost += distance_matrix[current_city][start_depot]
    return solution, cost

def choose_next_city(current_city, unvisited):
    probabilities = pheromone[current_city][unvisited] ** alpha * heuristic[current_city][unvisited] ** beta
    probabilities /= probabilities.sum()
    return unvisited[np.random.choice(len(unvisited), p=probabilities)]

# Execute the ACO
best_solutions, best_costs = ant_colony_optimization()
total_travel_cost = sum(best_costs)
print("Optimal tours and costs for each robot:")
for i, (solution, cost) in enumerate(zip(best_solutions, best_costs)):
    print(f"Robot {i} Tour: {solution}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")