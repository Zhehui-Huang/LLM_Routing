import numpy as np
import random

# Define the number of robots and cities
num_robots = 4
num_cities = 22

# City locations
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_values[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial population
def generate_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        # Create a valid split chromosome per robot
        all_cities = list(range(num_cities))
        random.shuffle(all_cities)
        divider_indices = sorted(random.sample(range(1, num_cities), num_robots - 1))
        robot_tours = [all_cities[i:j] for i, j in zip([0] + divider_indices, divider_indices + [None])]
        population.append(robot_tours)
    return population

# Calculate total cost for one solution
def calculate_total_cost(solution):
    total_cost = 0
    starting_city = city_coordinates[0] # All start at Depot 0 index coordinate
    for tour in solution:
        current_city = starting_city
        for city in tour:
            total_cost += distance(currentai])]
            current_city = city
        # Cost from last city back to the respective depot
        total_cost += distance(current_city, starting_city)
    return total_cost

# Genetic Algorithm Parameters
pop_size = 100
G_max = 500
mutation_rate = 0.15
crossover_rate = 0.8

# GA main loop
def genetic_algorithm():
    population = generate_population(pop_size, num_cities, num_robots)
    best_cost = float('inf')
    best_solution = None

    for generation in range(G_max):
        # Evaluate population
        fitness_scores = [calculate_total_cost(member) for member in population]

        # Check for new best solution
        for sol, score in zip(population, fitness_scores):
            if score < best_cost:
                best_cost = score
                best_solution = sol
        
        # Selection (roulette wheel or tournament)
        # Roulette Wheel Selection
        fitness_scores = [1/x for x in fitness_scores]
        total_fitness = sum(fitness_scores)
        probabilities = [f/total_fitness for f in fitness_scores]
        selected_indices = np.random.choice(range(pop_size), size=pop_size, p=probabilities)
        selected_population = [population[i] for i in selected_indices]
        
        # Crossover
        next_population = []
        for _ in range(0, pop_size, 2):
            if random.random() < crossover_rate:
                # Using simple one-point crossover for simplicity
                parent1 = selected_population[_]
                parent2 = selected_population[_+1]
                cut = random.randint(0, num_cities-1)
                child1 = parent1[:cut] + parent2[cut:]
                child2 = parent2[:cut] + parent1[cut:]
                next_population.extend([child1, child2])
            else:
                next_population.extend([selected_population[_], selected_population[_+1]])
        
        # Mutation
        for individual in next_population:
            if random.random() < mutation_rate:
                i, j = random.sample(range(num_cities), 2)
                individual[i], individual[j] = individual[j], individual[i]

        population = next_population

    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()

print("Optimal Solution Tours with total minimum cost:")
for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: [0] + {tour} + [0]")
    print(f"Robot {i} Total Travel Cost: {calculate_total_cost([tour])}")
print(f"Overall Total Travel Cost: {best_cost}")