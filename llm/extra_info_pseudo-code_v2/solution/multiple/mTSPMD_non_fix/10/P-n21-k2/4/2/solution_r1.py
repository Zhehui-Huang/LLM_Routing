import numpy as_np
import random

# City coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(coordinates[city1]) - np.array(coordinates[city2]))

# Genetic Algorithm Parameters
num_generations = 200
population_size = 50
mutation_rate = 0.10
crossover_rate = 0.85

# Number of robots and their corresponding depots
num_robots = 2
depots = [0, 1]

# Exclude depots from the list of cities
cities = list(range(len(coordinates)))
for depot in depots:
    cities.remove(depot)

def generate_initial_population(pop_size, cities, num_robots):
    population = []
    for _ in range(pop_size):
        remaining_cities = cities[:]
        random.shuffle(remaining_cities)
        split_points = sorted(random.sample(range(1, len(remaining_cities)), num_robots - 1))
        tours = []
        prev = 0
        for i in range(num_robots):
            next_split = split_points[i] if i < len(split_points) else len(remaining_cities)
            tours.append([depots[min(i, len(depots) - 1)]] + remaining_cities[prev:next_split])
            prev = next_split
        population.append(tours)
    return population

def calculate_total_cost(tours):
    return sum(sum(euclidean_distance(tours[i][j], tours[i][j+1]) for j in range(len(tours[i])-1)) for i in range(len(tours)))

def evaluate_population(population):
    return [calculate_total_cost(individual) for individual in population]

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1, parent2]
    point1 = random.randint(1, len(parent1) - 1)
    point2 = random.randint(1, len(parent2) - 1)
    child1 = [parent1[:point1] + parent2[point2:]]
    child2 = [parent2[:point2] + parent1[point1:]]
    return [child1, child2]

def mutate(tour):
    if random.random() > mutation_rate:
        return tour
    i, j = random.sample(range(1, len(tour) - 1), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm():
    population = generate_initial_population(population_size, cities, num_robots)
    best_cost = float('inf')
    best_solution = None

    for _ in range(num_generations):
        fitness_scores = evaluate_population(population)
        sorted_idx = np.argsort(fitness_scores)
        if fitness_scores[sorted_idx[0]] < best_cost:
            best_cost = fitness_scores[sorted_idx[0]]
            best_solution = population[sorted_idx[0]]

        new_population = [population[idx] for idx in sorted_idx[:population_size // 2]]

        while len(new_population) < population_size:
            if random.random() < crossover_rate:
                parents = random.sample(new_population, 2)
                for child in crossover(parents[0], parents[1]):
                    new_population.append(mutate(child[0]) if random.random() < mutation_rate else child[0])
            if len(new_population) > population_size:
                break
        
        population = new_population[:population_size]

    return best_solution, best_cost

# Running the genetic algorithm and printing out the optimal tours and costs
solution, total_cost = genetic_algorithm()
print("Optimal Tours and Costs:")
for idx, tour in enumerate(solution):
    # Adjust the last city to the correct depot for each robot
    last_city = tour[-1]
    next_depot = depots[idx] if idx < len(depots) else depots[-1]
    if last_city != next_depot:
        tour.append(next_depot)
    tour_cost = calculate_total_cost([tour])
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {total_cost}")