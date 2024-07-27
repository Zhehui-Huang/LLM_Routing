import numpy as np
import random

# Define the city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def fitness(route):
    # Calculate the total traveling distance of the route
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += distance(route[i-1], route[i])
    total_distance += distance(route[-1], route[0])  # Return to the starting point
    return total_distance

def create_random_route(num_cities, num_robots):
    base_route = list(range(1, num_cities))  # Starting from 1 because 0 is the depot
    random.shuffle(base_route)
    splits = sorted(random.sample(range(1, num_cities-1), num_robots-1))
    routes = [base_route[i:j] for i, j in zip([0] + splits, splits + [None])]
    routes = [[0] + route for route in routes]  # Start each route from depot 0
    return routes

def crossover(route1, route2):
    # Single-point crossover
    point = random.randint(1, len(route1)-2)
    child = route1[:point] + [city for city in route2 if city not in route1[:point]]
    return child

def mutate(route, mutation_rate=0.01):
    for swap in range(len(route)):
        if random.random() < mutation_rate:
            swap_with = random.randint(1, len(route)-1)
            route[swap], route[swap_with] = route[swap_with], route[swap]

def genetic_algorithm(num_cities, num_robots, population_size, num_generations, mutation_rate=0.01):
    population = [create_random_route(num_cities, num_robots) for _ in range(population_size)]
    best_route = None
    best_distance = float('inf')
    
    for generation in range(num_generations):
        # Evaluate the population
        fitnesses = [sum(fitness(route) for route in individual) for individual in population]
        current_best = population[np.argmin(fitnesses)]
        current_best_distance = min(fitnesses)
        
        if current_best_distance < best_distance:
            best_route = current_best
            best_distance = current_best_distance
        
        # Selection based on roulette wheel
        fitness_scores = [1/f for f in fitnesses]
        total_fitness = sum(fitness_scores)
        probabilities = [f/total_fitness for f in fitness_scores]
        selected_indices = np.random.choice(range(population_size), size=population_size, p=probabilities)
        selected_population = [population[i] for i in selected_indices]
        
        # Crossover and mutation
        next_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_population[i], selected_population[(i+1) % population_size]
            for child in (crossover(parent1, parent2), crossover(parent2, parent1)):
                mutate(child, mutation_rate)
                next_population.append(child)
        
        population = next_population
    
    return best_route, best_distance

# Parameters
num_cities = 22
num_robots = 4
population_size = 100
num_generations = 500
mutation_rate = 0.02

best_solution, best_cost = genetic_algorithm(num_cities, num_robots, population_size, num_generations, mutation_rate)

# Output formats
print("Optimal Solution Tours with total minimum cost:")
for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {fitness(tour)}")
print(f"Overall Total Travel Cost: {best_cost}")