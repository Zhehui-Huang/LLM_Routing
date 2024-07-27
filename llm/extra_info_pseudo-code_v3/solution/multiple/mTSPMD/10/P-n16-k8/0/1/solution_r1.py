import numpy as np
import random

# Coordinates for each city including depots
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Individual for GA
class Individual():
    def __init__(self, route):
        self.route = route
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        cost = 0
        for idx in range(len(self.route)-1):
            cost += calculate_distance(self.route[idx], self.route[idx+1])
        return cost

# GA operations
def generate_initial_population(size, depot, cities):
    population = []
    for _ in range(size):
        tour = cities.copy()
        random.shuffle(tour)
        population.append(Individual([depot] + tour + [depot]))
    return population

def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: x.cost)
    return selected[0]

def ordered_crossover(parent1, parent2):
    p1, p2 = [], []
    geneA = int(random.random() * len(parent1.route))
    geneB = int(random.random() * len(parent1.route))

    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    for i in range(start_gene, end_gene):
        p1.append(parent1.route[i])
    
    p2 = [item for item in parent2.route if item not in p1]

    return Individual(parent1.route[:start_gene] + p1 + parent2.route[end_gene:])

def mutate(individual, mutation_rate):
    for swapped in range(len(individual.route)):
        if(random.random() < mutation_rate):
            swap_with = int(random.random() * len(individual.route))
            
            city1 = individual.route[swapped]
            city2 = individual.route[swap_with]
            
            individual.route[swapped] = city2
            individual.route[swap_with] = city1
    individual.cost = individual.calculate_cost()

# Main GA execution
def genetic_algorithm(depot, cities, population_size, generations, mutation_rate):
    population = generate_initial_population(population_size, depot, cities)
    best_route = None
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = ordered_crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    
    # Sort to find the best route
    population.sort(key=lambda x: x.cost)
    best_route = population[0]
    return best_depot_route

# Assign cities to robots
depots = [0, 1, 2, 3, 4, 5, 6, 7]
cities = [8, 9, 10, 11, 12, 13, 14, 15]
num_robots = 8

# Solve the problem using GA for each robot
results = []

for robot_id in range(num_robots):
    depot = depots[robot_id]
    assigned_cities = [city for city in cities if city % num_robots == robot_id % num_robots]
    best_route = genetic_algorithm(depot, assigned_cities, 100, 100, 0.01)
    results.append((robot_id, best_route.route, best_route.cost))

# Display results
overall_total_cost = 0
for result in results:
    robot_id, tour, cost = result
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total_cost}")