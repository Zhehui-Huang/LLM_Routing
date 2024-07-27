import numpy as np
import random
from scipy.spatial import distance_matrix

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

robot_depots = [0, 1, 2, 3]
num_robots = 4

# Generate the distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = distance_matrix(coordinates, coordinates)

# Genetic Algorithm Parameters
population_size = 100
generations = 1000
mutation_rate = 0.1
tournament_size = 5

def create_initial_population():
    population = []
    all_cities = list(cities.keys())
    
    for _ in range(population_size):
        # Robots split the cities randomly including their start & end depots
        shuffled_cities = random.sample(all_cities, len(all_cities))
        # Ensure depots are not moved
        for dep in robot_depots:
            shuffled_cities.remove(dep)
        random.shuffle(shuffled_cities)
        for dep in sorted(robot_depots, reverse=True):
            shuffled_cities.insert(0, dep)
        population.append(shuffled_cities)
        
    return population

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[tour[i], tour[i+1]]
    total_cost += dist_matrix[tour[-1], tour[0]]  # Returning to the start
    return total_cost

def crossover(parent1, parent2):
    # Implementing Ordered Crossover (OX)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    middle = parent1[start:end + 1]
    child[start:end + 1] = middle
    
    fill_positions = list(range(start)) + list(range(end + 1, len(parent1)))
    fill_values = [city for city in parent2 if city not in middle]
    
    for position, value in zip(fill_positions, fill_values):
        child[position] = value
    
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

def select_parents(population):
    # Tournament Selection
    best = None
    for _ in range(tournament z_size):
        ind = random.choice(population)
        if best is None or calculate_cost(ind) < calculate_cost(best):
            best = ind
    return best

# Genetic Algorithm Execution
population = create_initial_population()

for generation in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = select_parents(population)
        parent2 = select_parents(population)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])
    population = new_population

# Evaluation
best_solution = min(population, key=calculate_cost)
total_cost = calculate_cost(best_solution)

# Determine tours for each robot based on their respective depots
robot_tours = {depot: [depot] for depot in robot_depots}
current_robot = 0

for city in best_solution[1:]:  # Skip initial attachment to depot
    if city in robot_depots:
        current_robot = robot_depots.index(city)
    robot_tours[robot_depots[current_robot]].append(city)

# Display tours and costs
total_travel_cost = 0

for robot, tour in robot_tours.items():
    robot_cost = calculate_cost(tour)
    total_travel_cost += robot_cost
    print(f"Robot {robot_depots.index(robot)} Tour: {tour}")
    print(f"Robot {robot_depots.index(robot)} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")