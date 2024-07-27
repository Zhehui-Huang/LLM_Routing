import numpy as np
import random

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities, depots, and robots
num_cities = len(coordinates)
num_depots = 8  # Number of starting depot cities
num_robots = num_depots  # Same as number of depots

# Parameters for the ACO algorithm
antnum = 30  # Number of ants (robots)
cyclenum = 100  # Number of cycles
inittrail = 1.0  # Initial pheromone level
alpha = 1  # Pheromone influence
beta = 2  # Distance influence
rho = 0.1  # Pheromone decay rate

# Distance matrix computation
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = np.array([
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
])

# Inverse of distance for heuristic information
eta = 1 / (distance_matrix + 0.1)  # Adding 0.1 to avoid division by zero

# Pheromone matrix initialization
pheromone = np.full((num_cities, num_cities), inittrail)

def reset_pheromone():
    global pheromone
    pheromone = np.full((num_cities, num_cities), inittrail)

def aco_tsp():
    global pheromone
    best_cost = float('inf')
    best_solution = None
    
    for cycle in range(cyclenum):
        solutions = []
        for ant in range(antnum):
            start_city = ant % num_depots
            tour = [start_city]
            current_city = start_city
            remaining_cities = set(range(num_cities)) - {start_city}
            
            while remaining_cities:
                transition_probs = [
                    (pheromone[current_city][j]**alpha * eta[current_city][j]**beta if j in remaining_cities else 0)
                    for j in range(num_cities)
                ]
                total_prob = sum(transition_probs)
                if total_prob == 0:
                    break  # Avoid division by zero if total_prob is zero
                transition_probs = [p / total_prob for p in transition_probs]
                next_city = np.random.choice(range(num_cities), p=transition_probs)
                tour.append(next_city)
                remaining_cities.remove(next_city)
                current_city = next_city
            
            tour.append(start_city)  # Return to the starting depot at the end
            
            # Calculate total cost of the tour
            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            solutions.append((tour, tour_cost))
        
        # Update pheromones
        pheromone *= (1 - rho)
        for tour, cost in solutions:
            for i in range(len(tour)-1):
                pheromone[tour[i]][tour[i+1]] += 1 / cost
        
        # Check for the best solution in this cycle
        cycle_best_tour, cycle_best_cost = min(solutions, key=lambda x: x[1])
        if cycle_best_cost < best_cost:
            best_cost = cycle_best_cost
            best_solution = cycle_best_tour
    
    return best_solution, best_cost

best_solution, total_cost = aco_tsp()

# Formatting the output as specified
robot_tours = [[] for _ in range(num_robots)]
robot_costs = [0] * num_robots

for i in range(len(best_solution) - 1):
    robot_id = i % num_robots
    robot_tours[robot_id].append(best_solution[i])
    robot_costs[robot_id] += distance_matrix[best_solution[i]][best_solution[i+1]]

output_str = []
for robot_id in range(num_robots):
    output_str.append(f"Robot {robot_id} Tour: {robot_tours[robot_id] + [robot_tours[robot_id][0]]}")
    output_str.append(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

output_str.append(f"Overall Total Travel Cost: {sum(robot_costs)}")

for line in output_str:
    print(line)