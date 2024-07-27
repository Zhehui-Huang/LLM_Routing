import random
import numpy as np

# City coordinates (index correspond to the city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots and their depots
depots = [0, 1, 2, 3]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def create_chromosome(num_cities, num_robots):
    # Creates a random chromosome while maintaining the depot initial and final positions for each robot
    city_indices = list(range(num_cities))
    random.shuffle(city_indices)
    segments = np.array_split(city_indices, num_robots)
    return [item for sublist in segments for item in sublist]

def decode_chromosome(chromosome, num_robots):
    # Assemble tours for each robot
    size = len(chromosome) // num_robots
    tours = {}
    for i in range(num_robots):
        tour = [depots[i]] + chromosome[i*size:(i+1)*size] + [depots[i]]
        tours[i] = tour
    return tours

def fitness(chromosome, num_robots):
    tours = decode_chromosome(chromosome, num_robots)
    return sum(total_distance(tour) for tour in tours.values())

def mutate(chromosome, mutation_rate=0.05):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(num_generations=100, population_size=50, num_robots=4):
    num_cities = len(coordinates) - num_robots
    population = [create_chromosome(num_cities, num_robots) for _ in range(population_size)]

    for generation in range(num_generations):
        population = sorted(population, key=lambda x: fitness(x, num_robots))
        next_generation = population[:2]  # Elitism

        # Generate new offspring
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)

        population = next_generation

    best_solution = min(population, key=lambda x: fitness(x, num_robots))
    return decode_chromosome(best_solution, num_robots)

# Running the genetic algorithm to solve the problem
best_tours = genetic_algorithm()

# Output the results
overall_total_cost = 0
for robot_id, tour in best_tours.items():
    cost = total_distance(tour)
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")