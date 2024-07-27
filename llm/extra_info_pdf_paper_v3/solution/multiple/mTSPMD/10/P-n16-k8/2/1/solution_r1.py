import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = euclidean_distance(i, j)

# Robot information and depot mapping
robot_start_end = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
num_robots = len(robot_start_end)

# Genetic Algorithm Parameters
population_size = 50
generations = 500
mutation_rate = 0.1
tournament_size = 5

# Initial random population
def create_initial_population():
    population = []
    for _ in range(population_size):
        # Create random tours for each robot
        all_cities = list(range(len(cities)))
        for depot in robot_start_end.values():
            all_cities.remove(depot)
        
        random.shuffle(all_cities)
        segments = np.array_split(all_cities, num_robots)
        
        tours = []
        for robot_id in range(num_robots):
            tour = [robot_start_end[robot_id]] + list(segments[robot_id]) + [robot_start_end[robot_id]]
            tours.append(tour)
        population.append(tours)
    return population

# Calculate total cost of tours for a solution
def calculate_cost(solution):
    total_cost = 0
    for tour in solution:
        for i in range(len(tour) - 1):
            total_cost += distance_matrix[tour[i], tour[i+1]]
    return total_cost

# Tournament selection
def tournament_selection(population):
    best = None
    for _ in range(tournament_size):
        ind = random.choice(population)
        if best is None or calculate_cost(ind) < calculate_cost(best):
            best = ind
    return best

# Two-point crossover
def crossover(parent1, parent2):
    child = []
    for i in range(num_robots):
        start, end = sorted(random.sample(range(len(parent1[i])), 2))
        middle = parent1[i][start:end]
        
        child_tour = [city for city in parent2[i] if city not in middle]
        child.append(child_tour[:start] + middle + child_tour[start:])
    return child

# Mutate a solution
def mutate(solution):
    for tour in solution:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour) - 1), 2)
            tour[i], tour[j] = tour[j], tour[i]

# Genetic Algorithm
def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    
    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = tournament_selection(population), tournament_selection(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        
        population = new_population
        
        # Elitism: Keep the best found solution
        current_best = min(population, key=calculate_cost)
        if best_solution is None or calculate_cost(current_best) < calculate_cost(best_solution):
            best_solution = current_best

    return best_solution

# Run the Genetic Algorithm and output results
best_tours = genetic_algorithm()
overall_cost = calculate_cost(best_tours)

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {best_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {calculate_cost([best_tours[i]])}")
print(f"Overall Total Travel Cost: {overall_cost}")