import random
import numpy as np

# City coordinates (index corresponds to the city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots and their depots
robots = {0: 0, 1: 1, 2: 2, 3: 3}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def fitness(chromosome):
    total_dist = 0
    tours = decode_chromosome(chromosome)
    for tour in tours.values():
        total_dist += total_distance(tour)
    return total_dist

def crossover(parent1, parent2):
    """ Perform OX crossover """
    size = len(parent1)
    start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
    child = [None] * size
    
    # Copy a slice from first parent:
    child[start:end + 1] = parent1[start:end + 1]
    
    # Fill using second parent
    p2_idx = 0
    for i in range(size):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child

def mutate(chromosome):
    """ Perform swap mutation """
    idx1, idx2 = random.sample(range(len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

def decode_chromosome(chromosome):
    """ Decode chromosome into tours for each robot """
    cities_per_robot = {r: [robots[r]] for r in robots}
    assignment = chromosome[len(robots):]
    for city, robot in zip(cities_per_robot, assignment):
        cities_per_robot[robot].append(city if city > 3 else city + 4)
    for robot in cities_per_robot:
        cities_per_robot[robot].append(robots[robot])
    return cities_per_robot

def generate_initial_population(size, city_list):
    population = []
    for _ in range(size):
        shuffled_cities = random.sample(city_list, len(city_list))
        population.append(shuffled_cities)
    return population

def genetic_algorithm(cities, population_size=100, generations=500):
    # Generate initial population
    city_list = list(range(4, len(coordinates)))  # non-depot cities
    population = generate_initial_population(population_size, city_list)
    
    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        next_generation = population[:2]  # elitism: carry over the best two solutions
        
        # Generate new individuals
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)  # tournament selection from top 50
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # mutation probability
                mutate(child)
            next_generation.append(child)
        
        population = next_generation
    
    best_solution = min(population, key=lambda x: fitness(x))
    return decode_chromosome(best_solution)

# Execute the genetic algorithm
best_tours = genetic_algorithm(coordinates)

# Calculate and print the tours for each robot and total cost
total_cost = 0
for robot_id, tour in best_tours.items():
    cost = total_distance(tour)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")