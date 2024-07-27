import numpy as np
from scipy.spatial.distance import euclidean

# Define city coordinates and number of robots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
num_robots = 8
depots = list(range(num_robots))

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j]) if i != j else float('inf')
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Around 10 iterations and 20 ants in the colony for testing
iterations = 10
num_ants = 20
alpha = 1.0
beta = 5.0
evaporation_rate = 0.1
initial_pheromone = 1 / (np.max(distance_matrix) * len(cities))

pheromones = np.full(distance_matrix.shape, initial_pheromone)
best_cost = np.inf
best_tours = None

def choose_next_city(current_city, unvisited, pheromones, distance_matrix):
    probabilities = []
    pheromone_list = pheromones[current_city][unvisited]
    heuristic_list = 1 / distance_matrix[current_city][unvisited]
    probabilities = pheromone_list**alpha * heuristic_list**beta
    probabilities /= probabilities.sum()
    return np.random.choice(unvisited, p=probabilities)

for iteration in range(iterations):
    all_tours = []
    all_costs = []
    
    for ant in range(num_ants):
        tours = []
        costs = []
        
        # Assign each robot a starting city and let it complete a tour
        for dep in depots:
            tour = [dep]
            current_city = dep
            unvisited = set(cities.keys()) - set(tour)
            
            while unvisited:
                next_city = choose_next_city(current_city, list(unvisited), pheromones, distance_matrix)
                tour.append(next_city)
                current_city = next_city
                unvisited.remove(next_city)
            
            tour.append(dep)  # Return to depot
            tours.append(tour)
            cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            costs.append(cost)
        
        all_tours.append(tours)
        all_costs.append(costs)
        
        # Update pheromones for this ant's solution
        this_sol_pheromone = evaporation_rate / sum(costs)
        for tour in tours:
            for i in range(len(tour)-1):
                pheromones[tour[i]][tour[i+1]] += this_sol_pheromone

    # Pheromone evaporation
    pheromones *= (1 - evaporation_rate)
    
    # Check if the current solution is the best
    for i in range(num_ants):
        total_cost = sum(all_costs[i])
        if total_cost < best_cost:
            best_cost = total_cost
            best_tours = all_tours[i]

# Output the best solution
print(f"Overall Total Travel Cost: {best_cost}")
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {best_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {sum(distance_matrix[best_tours[robot_id][i]][best_tours[robot_id][i+1]] for i in range(len(best_tours[robot_id])-1))}")