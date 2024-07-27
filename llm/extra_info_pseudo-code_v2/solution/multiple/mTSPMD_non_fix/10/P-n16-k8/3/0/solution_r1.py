import numpy as np
import random
import math

# Coordinates of cities and depots
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

num_robots = 8
depot = 0  # All robots start at depot city 0

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((coords[p1][0] - coords[p2][0]) ** 2 + (coords[p1][1] - coords[p2][1]) ** 2)

# Generate initial population of solutions
def generate_initial_solutions(pop_size=100):
    population = []
    cities = list(range(1, len(coords)))  # all cities except the starting depot

    for _ in range(pop_size):
        random.shuffle(cities)
        # cut the shuffled cities into chunks for each robot
        parts = []
        for i in range(num_robots):
            size = len(cities) // num_robots + (1 if i < len(cities) % num_robots else 0)
            start_index = sum([len(parts[j]) for j in range(i)])
            parts.append([depot] + cities[start_index:start_index + size])
        population.append(parts)

    return population

# Calculate the cost of a single solution
def calculate_cost(solution):
    total_cost = 0
    costs = []
    for subroute in solution:
        subroute_cost = 0
        for i in range(len(subroute) - 1):
            subroute_cost += euclidean_data[subroute[i]][subroute[i + 1]]
        costs.append(subroute_cost)
        total_cost += subroute_cost
    return total_cost, costs

# Updating Genetic algorithm functions
def crossover(parent1, parent2):
    # Select random index for starting crossover and end index
    index1 = random.randint(1, len(parent1)-2)
    index2 = random.randint(index1, len(parent1)-1)

    # Performing two point crossover
    temp = parent1[index1:index2]
    new_p1 = [item for item in parent2 if item not in temp]
    child = new_p1[:index1] + temp + new_p1[index1:]
    return child

def mutate(solution, mutation_rate=0.01):
    for subroute in solution:
        for i in range(len(subroute)):
            if random.random() < mutation_rate:
                swap_with = random.randint(1, len(subroute) - 1)
                subroute[i], subroute[swap_with] = subroute[swap_with], subroute[i]

def genetic_algorithm(pop_size=100, generations=500, mutation_rate=0.01):
    population = generate_initial_solutions(pop_size)

    # Initial best solution
    best_solution = min(population, key=lambda sol: calculate_cost(sol)[0])
    best_cost = calculate_cost(best_solution)[0]

    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = [crossover(p1, p2) for p1, p2 in zip(parent1, parent2)]
            mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

        # Finding best solution in the current generation
        current_best = min(population, key=lambda sol: calculate_cost(sol)[0])
        current_cost = calculate_cost(current_best)[0]
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best

    return best_solution, best_cost

# Precompute the distances
euclidean_data = [[euclidean_distance(i, j) for j in range(len(coords))] for i in range(len(coords))]

# Running the genetic algorithm
final_solution, final_cost = genetic(actual_algorithm()
tour_costs, _ = calculate_cost(final_solution)

# Output results
for idx, tour in enumerate(final_solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")
print(f"Overall Total Travel Cost: {final_cost}")