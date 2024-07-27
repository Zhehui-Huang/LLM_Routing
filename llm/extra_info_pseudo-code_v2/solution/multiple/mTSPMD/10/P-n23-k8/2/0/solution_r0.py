import numpy as np
import random

# City coordinates and number of robots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]
robot_base_indices = [0, 1, 2, 3, 4, 5, 6, 7]

# Parameters
antnum = 50
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
num_robots = len(robot_base_indices)

# Distance and pheromone matrices
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
pheromones = np.full((num_cities, num_cities), init_pheromone)

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Initialize distances
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])
            
# Heuristic information (inverse distance)
heuristic_info = 1 / (distances + 1e-10)

# Calculate transition probabilities for ants
def transition_probabilities(ant_location, visited):
    allowed = [i for i in range(num_cities) if i not in visited]
    probabilities = []
    denominator = sum((pheromones[ant_location][j] ** alpha) * (heuristic_info[ant_location][j] ** beta) for j in allowed)
    for j in allowed:
        probabilities.append(((pheromones[ant_location][j] ** alpha) * (heuristic_info[ant_location][j] ** beta)) / denominator)
    return allowed, probabilities

# Perform the ACO algorithm
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    solutions = []
    for ant in range(antnum):
        robot = random.choice(robot_base_indices)
        tour = [robot]
        cost = 0
        visited = set(tour)
        current_city = robot
        
        while len(visited) < num_cities:
            possible_cities, probs = transition_probabilities(current_city, visited)
            if possible_cities:
                next_city = random.choices(possible_cities, weights=probs, k=1)[0]
                tour.append(next_city)
                cost += distances[current_city][next_city]
                visited.add(next_city)
                current_city = next_city
            else:
                break
    
        tour.append(robot)  # Return to depot
        cost += distances[current_city][robot]  # Cost to return to depot
        solutions.append((tour, cost))
    
    # Find the best solution in this cycle
    for solution, sol_cost in solutions:
        if sol_cost < best_cost:
            best_solution = solution
            best_cost = sol_cost
    
    # Update pheromones
    pheromones *= (1 - evaporation_rate)  # Evaporation
    for tour, cost in solutions:
        for i, city in enumerate(tour[:-1]):
            pheromones[city][tour[i + 1]] += 1 / cost  # Pheromone deposit

# Output the results in the specified format
print(f"Robot 0 Tour: {best_solution}")
print(f"Robot 0 Total Travel Cost: {best_cost}")
print(f"Overall Total Travel Cost: {best_cost}")