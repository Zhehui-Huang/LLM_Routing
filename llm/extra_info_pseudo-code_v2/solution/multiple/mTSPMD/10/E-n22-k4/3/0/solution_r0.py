import math
import random

# City Coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Distance calculation utility
def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0])**2 + (city_coordinates[city1][1] - city_coordinates[city2][1])**2)

# Parameters:
antnum = 10
cyclenum = 100
inittrail = 10.0
alpha = 1.0
beta = 5.0
rho = 0.05
number_of_cities = len(city_coordinates)
n_depots = 4
n_robots = n_depots

# Pheromone initialization
pheromone = [[inittrail for _ in range(number_of_cities)] for _ in range(number_of_cities)]
heuristic_info = [[1.0/max(1e-5,calculate_distance(i, j)) for j in range(number_of_cities)] for i in range(number_of_cities)]

# Main loop
best_solution = None
best_solution_length = float('inf')

for cycle in range(cyclenum):
    solutions = []
    for ant in range(antnum):
        tours = {robot: [robot] for robot in range(n_robots)}
        remaining_cities = set(range(n_depots, number_of_cities))
        while remaining_cities:
            for robot in range(n_robots):
                current_city = tours[robot][-1]
                if not remaining_cities:
                    break
                probabilities = []
                total_probability = 0
                for next_city in remaining_cities:
                    edge_prob = (pheromone[current_city][next_city]**alpha) * (heuristic_info[current_city][next_city]**beta)
                    probabilities.append((edge_prob, next_city))
                    total_probability += edge_prob
                probabilities = [(prob/total_probability, city) for prob, city in probabilities]
                next_city = max(probabilities, key=lambda x: x[0])[1]
                tours[robot].append(next_city)
                remaining_cities.remove(next_city)
        
        for robot in range(n_robots):
            tours[robot].append(robot)  # return to depot
        
        # Calculate solution length and update best solution if it's better
        solution_length = sum(calculate_distance(tours[robot][i], tours[robot][i+1]) for robot in range(n_robots) for i in range(len(tours[robot]) - 1))
        if solution_length < best_solution_length:
            best_solution_length = solution_length
            best_solution = tours
        
        solutions.append((tours, solution_length))
    
    # Update pheromones
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            pheromone[i][j] *= (1 - rho)
    
    for tours, length in solutions:
        contribution = 1.0 / length
        for robot in range(n_robots):
            for i in range(len(tours[robot]) - 1):
                pheromone[tours[robot][i]][tours[robot][i+1]] += contribution

# Output the results
overall_total_cost = 0
for robot in range(n_robots):
    tour_cost = sum(calculate_distance(best_solution[robot][i], best_solution[robot][i+1]) for i in range(len(best_solution[robot]) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {best_solution[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")