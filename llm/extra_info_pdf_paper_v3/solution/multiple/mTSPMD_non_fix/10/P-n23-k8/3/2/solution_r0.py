import numpy as np
import random
from scipy.spatial.distance import euclidean

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def generate_initial_solution(num_robots, cities):
    all_cities = list(range(len(cities)))
    random.shuffle(all_cities)
    chunk_size = len(cities) // num_robots
    return [all_cities[i * chunk_size:(i + 1) * chunk_size] for i in range(num_robots)]

def calculate_cost(tours):
    total_cost = 0
    detailed_costs = []
    for tour in tours:
        cost = 0
        if len(tour) > 1:
            for j in range(len(tour) - 1):
                cost += euclidean(coordinates[tour[j]], coordinates[tour[j + 1]])
            # cost to return to depot
            cost += euclidean(coordinates[tour[-1]], coordinates[tour[0]])
        detailed_costs.append(cost)
        total_cost += cost
    return total_cost, detailed_costs

def genetic_algorithm(num_robots=8, generations=100, population_size=50):
    population = [generate_initial_solution(num_robots, coordinates) for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(generations):
        # Evaluate
        scored_population = [(calculate_cost(solution)[0], solution) for solution in population]
        scored_population.sort(key=lambda x: x[0])
        if scored_population[0][0] < best_cost:
            best_cost, best_solution = scored_prompt[0]
        
        # Selection
        survivors = scored_population[:population_size // 2]
        
        # Crossover and Mutation
        new_generation = []
        while len(new_generation) < population_size:
            parent1, parent2 = random.sample([sol for _, sol in survivors], 2)
            if random.random() < 0.7:  # crossover chance
                child = crossover(parent1, parent2)
                if random.random() < 0.1:  # mutation chance
                    mutate(child)
                new_generation.append(child)
            else:
                new_generation.append(parent1)
                new_generation.append(parent2)
        
        population = new_generation
    
    return best_solution, best_cost

def main():
    best_solution, best_cost = genetic_algorithm()
    total_cost, detailed_costs = calculate_cost(best_solution)
    overall_total_cost = sum(detailed_costs)
    for robot_id, tour in enumerate(best_solution):
        print(f"Robot {robot.id} Tour: {tour}")
        print(f"Robot {robot.id} Total Travel Cost: {detailed_costs[robot_id]}")
    print(f"Overall Total Travel Cost: {overall_total_cost}")

main()