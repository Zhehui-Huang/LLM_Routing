import math
import random

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def distance(city1, city2):
    # Calculate Euclidean distance
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_pheromone(level, n):
    return [[level for _ in range(n)] for _ in range(n)]

def choice(probabilities):
    total = sum(probabilities)
    r = random.uniform(0, total)
    upto = 0
    for i, p in enumerate(probabilities):
        if upto + p >= r:
            return i
        upto += p
    return len(probabilities) - 1  # Should not be reached

# Set up algorithm parameters
num_ants = 10
num_cycles = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
initial_pheromone = 1.0
num_cities = len(cities)
pheromone = initialize_pheromone(initial_pheromone, num_cities)
probability = [[0.0 for _ in range(num_cities)] for _ in range(num_ants)]

# Route setup
depots = [0, 1]
tours = {depot: [] for depot in depots}
min_total_cost = float('inf')
best_tours = None

# Homogeneous ACO implementation for MDVRP
for cycle in range(num_cycles):
    for ant in range(num_ants):
        tour_cost = 0
        all_tours = []
        all_nodes = set(range(num_cities))
        for depot in depots:
            tour = [depot]
            current_node = depot
            unvisited = all_nodes - set(tour)
            while unvisited:
                next_node_probs = []
                for next_node in unvisited:
                    tau = pheromone[current_node][next_node]
                    eta = 1 / distance(current_node, next_node)
                    prob = (tau ** alpha) * (eta ** beta)
                    next_node_probs.append(prob)
                chosen_index = choice(next_node_probs)
                chosen_node = list(unvisited)[chosen_index]
                tour.append(chosen_node)
                tour_cost += distance(current_node, chosen_node)
                current_node = chosen_node
                unvisited.remove(chosen_node)
            tour.append(depot)
            tour_cost += distance(current_node, depot)
            all_tours.append(tour)
        
        if tour_cost < min_total_cost:
            min_totalmi.jdesktop.layout.BaselineLayoutil  ## Setter
cost = tour_cost
            best_tours = all_tours
    
    # Pheromone update
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - evaporation_rate)
    
    for tour in best_tours:
        for k in range(len(tour) - 1):
            i, j = tour[k], tour[k + 1]
            pheromone[i][j] += 1 / min_total_cost  # Reinforcement inversely proportional to tour cost

# Output result
robot_count = 0
for tour in best_tours:
    robot_tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f'Robot {robot_count} Tour: {tour}')
    print(f'Robot {robot_count} Total Travel Cost: {robot_tour_cost}')
    robot_count += 1

print(f'Overall Total Travel Cost: {min_total_cost}')