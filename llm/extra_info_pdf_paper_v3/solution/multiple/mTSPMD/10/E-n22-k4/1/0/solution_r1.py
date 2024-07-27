import random
import math

# City coordinates and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]
cities = list(range(4, 22))
num_robots = 4

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# GA Parameters
population_size = 100
generations = 500
mutation_rate = 0.02  # Adjust mutation rate for stability in results

# Initialize and define GA functions
def create_individual():
    random.shuffle(cities)
    parts = np.array_split(cities, num_robots)
    return [[depots[i]] + list(part) + [depots[i]] for i, part in enumerate(parts)]

def population_initialization():
    return [create_individual() for _ in range(population_size)]

def fitness(individual):
    return sum(distance(individual[i][j], individual[i][j+1]) for i in range(num_robots) for j in range(len(individual[i])-1))

def crossover(parent1, parent2):
    def cross(p1, p2):
        child = p1.copy()
        start, end = sorted(random.sample(range(1, len(p1) - 1), 2))
        middle = p2[start:end]
        fixed = set(middle)
        cpos = 0
        for item in child:
            if cpos == start:
                cpos = end
            if item not in fixed:
                child[cpos] = item
                cpos += 1
        child[start:end] = middle
        return child

    return [[p[0]] + cross(p[1:-1], q[1:-1]) + [p[-1]] for p, q in zip(parent1, parent2)]

def mutate(route):
    index1, index2 = random.sample(range(1, len(route) - 1), 2)  # Avoid depots
    route[index1], route[index2] = route[index2], route[index1]

def selection(population):
    population.sort(key=fitness)
    return population[:population_size]

# Genetic algorithm execution
population = population_initialization()
for _ in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parents = random.sample(population, 2)
        child = crossover(parents[0], parents[1])
        if random.random() < mutation_rate:
            for route in child:
                mutate(route)
        new_population.append(child)
    population = selection(new_population + population)

# Get the best result
best_solution = min(population, key=fitness)
best_cost = fitness(best_solution)

# Output the results
total_travel_cost = 0
for i in range(num_robots):
    robot_tour = best_solution[i]
    robot_cost = sum(distance(robot_tour[j], robot_tour[j+1]) for j in range(len(robot_tour)-1))
    total_travel_cost += robot_cost
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")