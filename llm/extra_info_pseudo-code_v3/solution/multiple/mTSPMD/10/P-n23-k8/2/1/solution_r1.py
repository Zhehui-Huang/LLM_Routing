import random
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def calculate_fitness(individual, coordinates, depots):
    cities = individual[0]
    partitions = individual[1]
    tour_start = 0
    total_cost = 0
    tours = []
    
    for robot_id, depot_id in enumerate(depots):
        tour_length = partitions[robot_id]
        tour = [depot_id] + cities[tour_start:tour_start + tour_length] + [depot_id]
        cost = total_tour_cost(tour, coordinates)
        tours.append((tour, cost))
        total_cost += cost
        tour_start += tour_length
        
    return total_cost, tours

def create_individual(city_nodes, depots, num_robots):
    cities = city_nodes.copy()
    random.shuffle(cities)
    partitions = [len(cities) // num_robots] * num_robots
    for i in range(len(cities) % num_robots):
        partitions[i] += 1
    return (cities, partitions)

def ordered_crossover(parent1, parent2):
    size = len(parent1[0])
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child_cities = parent1[0][:idx1] + parent2[0][idx1:idx2] + parent1[0][idx2:]
    child_partitions = parent1[1][:]
    return (child_cities, child_partitions)

def mutate(individual):
    cities = individual[0]
    idx1, idx2 = random.sample(range(len(cities)), 2)
    cities[idx1], cities[idx2] = cities[idx2], cities[idx1]

def genetic_algorithm(city_coords, depots, num_robots, generations=1000, population_size=100):
    city_nodes = [i for i in range(len(city_coords)) if i not in depots]
    population = [create_individual(city_nodes, depots, num_robots) for _ in range(population_size)]
    
    for generation in range(generations):
        new_population = []
        for j in range(population_size):
            parent1, parent2 = random.sample(population, 2)
            child = ordered_crossover(parent1, parent2)
            if random.random() < 0.15:
                mutate(child)
            new_population.append(child)
        
        fitness_scores = [(calculate_fitness(ind, city_coords, depots), ind) for ind in new_population]
        population = [ind for _, ind in sorted(fitness_score, key=lambda x: x[0][0])[:population_size]]
    
    best_solution = min((calculate_fitness(ind, city_coords, depots), ind) for ind in population)
    return best_solution

# Find the solution
solution = genetic_algorithm(city_coords, depots, num_robots)
total_cost, tours_and_costs = solution[0]

# Output results
for idx, (tour, cost) in enumerate(tours_and_costs):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")