import numpy as np
import random
import math

# Coordinates of the cities
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Parameters
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 2.0
rho = 0.1

# Depots and robots
depots = [0, 1, 2, 3]
num_robots = len(depots)

# Calculate distance matrix
def distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (city_coords[i][1] - city_coords[j][1])**2)

num_cities = len(city_coords)
dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Initialize pheromone levels
pheromone = [[inittrail for _ in range(num_cities)] for _ in range(num_cities)]

def calculate_transition_probabilities(ant_position, pheromone, visited, last_depot):
    probs = np.zeros(num_cities)
    denom = 0.0
    for j in range(num_cities):
        if j not in visited:
            denom += pheromone[ant_position][j]**alpha * ((1.0 / dist_matrix[ant_position][j])**beta if dist_matrix[ant_position][j] != 0 else 0)

    for j in range(num_cities):
        if j not in visited:
            probs[j] = (pheromone[ant_position][j]**alpha * ((1.0 / dist_matrix[ant_position][j])**beta if dist_matrix[ant_position][j] != 0 else 0)) / denom

    return probs

def construct_solution():
    robots_tours = {robot: [dep] for robot, dep in enumerate(depots)}
    all_visited = set(depots)

    for _ in range(num_robots):
        for robot_id in range(num_robots):
            depot = depots[robot_id]
            while len(set(robots_tours[robot_id])) < (num_cities + 1) // num_robots + 1:
                current_city = robots_tours[robot_id][-1]
                if len(all_visited) == num_cities:
                    break
                probabilities = calculate_transition_probabilities(current_city, pheromone, all_visited, depot)
                next_city = np.random.choice(range(num_cities), p=probabilities)
                robots_tours[robot_id].append(next_city)
                all_visited.add(next_city)
            robots_tours[robot_id].append(depot)

    return robots_tours

def update_pheromone(robots_tours):
    for i, row in enumerate(pheromone):
        for j, value in enumerate(row):
            pheromone[i][j] *= (1 - rho)
    
    for robot_id, tour in robots_tours.items():
        tour_length = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        contribution = 1.0 / tour_length if tour_length != 0 else 0
        for i in range(len(tour)-1):
            pheromone[tour[i]][tour[i+1]] += contribution

# Main ACO cycle
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    robots_tours = construct_solution()
    update_pheromone(robots_tours)

    # Calculate the total cost for the solution
    total_cost = 0
    for robot_id, tour in robots_tours.items():
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

    if total_cost < best_cost:
        best_cost = total_cost
        best_solution = robots_tours

    print(f"Overall Total Travel Cost: {total_cost}")

# Final best solution and its cost
print("\nBest solution:")
total_cost = 0
for robot_id, tour in best_solution.items():
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")