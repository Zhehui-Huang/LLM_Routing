import random
import math
from heapq import nlargest

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def calculate_fitness(individual, coordinates, depots):
    current_city = 0
    cities_per_robot = [individual[i+1] for i in range(len(depots))]
    total_cost = 0
    detailed_costs = []
    
    start_idx = 0
    for robot_id in range(len(depots)):
        tour_len = cities_per_robot[robot_id]
        if tour_len == 0:
            continue
        tour = [depots[robot_id]] + individual[0][start_idx:start_idx + tour_len] + [depots[robot_id]]
        cost = total_cost(tour, coordinates)
        detailed_costs.append((tour, cost))
        total_cost += cost
        start_idx += tour_len
        
    return total_cost, detailed_costs

def create_individual(city_nodes, depots, num_robots):
    cities = city_nodes.copy()
    random.shuffle(cities)
    partitions = random.sample(range(1, len(cities)), num_robots - 1)
    partitions.sort()
    partitions = [0] + partitions + [len(cities)]
    number_of_cities = [partitions[i+1] - partitions[i] for i in range(num_robots)]
    return (cities, number_of_cities)

def ordered_crossover(parent1, parent2):
    size = len(parent1[0])
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child_p1 = parent1[0][idx1:idx2]
    child = [None]*size
    child[idx1:idx2] = child_p1
    
    current_pos = idx2
    for gene in parent2[0]:
        if gene not in child_p1:
            if current_pos >= size:
                current_pos = 0
            child[current_pos] = gene
            current_pos += 1
            
    num_cities_child = parent1[1][:]
    random.shuffle(num_cities_child)
    return (child, num_cities_child)

def mutate(individual):
    size = len(individual[0])
    idx1, idx2 = random.sample(range(size), 2)
    individual[0][idx1], individual[0][idx2] = individual[0][idx2], individual[0][idx1]

def genetic_algorithm(city_coords, depots, num_robots, generations=1000, population_size=100):
    city_nodes = list(range(len(city_coords)))
    population = [create_individual(city_nodes, depots, num_robots) for _ in range(population_size)]
    
    for generation in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(population, 2)
            child = ordered_crossover(parent1, parent2)
            if random.random() < 0.1:
                mutate(child)
            new_population.append(child)
        
        fitness_scores = [(calculate_fitness(ind, city_coords, depots), ind) for ind in new_population]
        population = [ind for _, ind in nlargest(population_size, fitness_scores, key=lambda x: x[0][0])]
    
    best_solution = min((calculate_fitness(ind, city_coords, depots), ind) for ind in population)
    return best_solution

# Set up the environment and robots
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = 8

# Find the solution
solution = genetic_algorithm(city_coords, depots, num_robots)
total_cost, tours_and_costs = solution[0]

for idx, (tour, cost) in enumerate(tours_and_cost):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")