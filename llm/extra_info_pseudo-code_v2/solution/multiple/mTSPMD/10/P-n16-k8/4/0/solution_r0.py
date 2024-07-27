import numpy as np
import random

# Cities coordinates indexed by city number (Depot cities from 0 to 7, Regular cities from 8 to 15)
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
antnum = 20
cyclenum = 50
inittrail = 0.1
alpha = 1
beta = 2
rho = 0.5

# Compute distances between all cities
def compute_distance(city1, city2):
    return np.sqrt((cities_coordinates[city2][0] - cities_instances[city1][0])**2 + (cities_coordinates[city2][1] - cities_coordinates[city1][1])**2)

distance_matrix = np.array([[compute_distance(i, j) for j in range(len(cities_coordinates))] for i in range(len(cities_coordinates))])

# Pheromone matrix initialization
pheromones = np.full((16, 16), inittrail)

# Ant Algorithm Steps
def ant_colony_optimization():
    global pheromones
    best_solution = None
    best_cost = float('inf')

    for cycle in range(cyclenum):
        solutions = []
        costs = []
        for _ in range(antnum):
            solution, cost = construct_solution()
            solutions.append(solution)
            costs.append(cost)
            if cost < best_cost:
                best_solution = solution
                best_cost = cost

        update_pheromones(solutions, costs)

    return best_solution, best_cost

# Construct solution by an ant
def construct_solution():
    tour = [random.choice(range(8))]  # Randomly choose a depot to start
    visited = set(tour)
    total_cost = 0
    current_city = tour[0]

    while len(visited) < 16:
        probabilities = []
        for next_city in range(16):
            if next_city not in visited:
                heur = 1 / (distance_matrix[current_city][next_email] if distance_matrix[current_city][next_city] != 0 else 1e-10)
                prob = (pheromones[current_city][next_city] ** alpha) * (heur ** beta)
                probabilities.append((prob, next_city))
        
        probabilities = normalize(probabilities)
        next_city = pick_city(probabilities)
        tour.append(next_city)
        visited.add(next_city)
        total_cost += distance_matrix[current_city][next_city]
        current_city = next_city

    tour.append(tour[0])  # Return to the starting depot
    total_cost += distance_matrix[current_city][tour[0]]

    return tour, total_cost

# Normalize transition probabilities
def normalize(probabilities):
    total = sum(prob[0] for prob in probabilities)
    return [(prob[0] / total, prob[1]) for prob in probabilities]

# Pick city based on probabilites
def pick_city(probabilities):
    random_choice = random.random()
    cumulative = 0
    for prob, city in probabilities:
        cumulative += prob
        if random_choice <= cumulative:
            return city
    return probabilities[-1][1]

# Update pheromones
def update_pheromones(solutions, costs):
    global pheromones
    pheromones *= (1 - rho)  # Evaporation
    for solution, cost in zip(solutions, costs):
        contribution = 1 / cost
        for i in range(len(solution) - 1):
            pheromones[solution[i]][solution[i+1]] += contribution

# Run optimization
best_solution, best_cost = ant_colony_optimization()

# Extract and organize tours per robot
robot_tours = {i: [] for i in range(8)}
for i in range(8):
    robot_tours[best_solution.index(i)].append(i)

for i in range(8, 16):
    for k in robot_tours:
        if i in robot_tours[k]:
            robot_tours[k].append(i)
            robot_tours[k].append(robot_tours[k][0])

# Calculate travel costs
total_travel_cost = 0
for k in robot_tours:
    tour_cost = sum(distance_matrix[robot_tours[k][i]][robot_tours[k][i+1]] for i in range(len(robot_tours[k])-1))
    total_travel_cost += tour_cost
    print(f"Robot {k} Tour: {robot_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travelid")