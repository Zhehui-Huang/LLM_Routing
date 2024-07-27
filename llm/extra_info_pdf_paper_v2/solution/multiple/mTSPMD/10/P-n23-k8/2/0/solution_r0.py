import numpy as np
import math

# defining the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Calculate distance matrix
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # To avoid selecting the same city

# Ant Colony Optimization parameters
num_ants = 30
num_iterations = 100
decay = 0.9
alpha = 1.0  # Pheromone importance
beta = 5.0  # Distance priority
Q = 10.0  # Pheromone deposition amount

# Pheromone matrix
pheromones = np.ones((num_cities, num_cities)) * 0.1

# implementing ACO
def aco():
    best_cost = float('inf')
    best_solution = []
    
    for iteration in range(num_iterations):
        all_solutions = []
        all_costs = []
        
        for ant in range(num_ants):
            start_depot = ant % 8  # alternating start depots
            tour = [start_depot]
            unvisited = list(set(cities.keys()) - set(tour))
            
            while unvisited:
                current_city = tour[-1]
                
                probabilities = []
                for next_city in unvisited:
                    pheromone = pheromones[current_city][next_city] ** alpha
                    inv_distance = (1.0 / distance_matrix[current_city][next_city]) ** beta
                    probabilities.append(pheromone * inv_distance)
                
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(unvisited, p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
            
            # Returning to the start depot
            tour.append(start_depot)

            # Calculate the travel cost of the tour
            cost = 0
            for i in range(len(tour) - 1):
                cost += distance_matrix[tour[i]][tour[i+1]]
                
            if cost < best_cost:
                best_cost = cost
                best_solution = tour[:]
            
            all_solutions.append(tour)
            all_costs.append(cost)
        
        # Pheromone decay
        for i in range(num_cities):
            for j in range(num_cities):
                pheromones[i][j] *= decay
        
        # Pheromone update
        for i in range(num_ants):
            for j in range(len(all_solutions[i]) - 1):
                pheromones[all_solutions[i][j]][all_solutions[i][j+1]] += Q / all_costs[i]
    
    return best_solution, best_cost

best_solution, best_cost = aco()

# Extract individual tours for each robot
robot_tours = {i: [] for i in range(8)}
current_robot = 0

# since each tour starts and ends at a depot, we split the best_solution accordingly
for i in range(1, len(best_solution)):
    if best_solution[i] < 8:  # signifies it's a depot
        current_robot = best_solution[i]
    else:
        robot_tours[current_robot].append(best_solution[i])

# Removing duplicates due to redundant back and forth to depots if needed
for robot, tour in robot_tours.items():
    seen = set()
    unique_tour = []
    for city in tour:
        if city not in seen:
            seen.add(city)
            unique_tour.append(city)
    robot_tours[robot] = unique_tour

# Get total travel cost for each robot
robot_costs = {}
total_cost = 0
for robot, tour in robot_tours.items():
    tour = [robot] + tour + [robot]  # start and end at the robot's depot
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")