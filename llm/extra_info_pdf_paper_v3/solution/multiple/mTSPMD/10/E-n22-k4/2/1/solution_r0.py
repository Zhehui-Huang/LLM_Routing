import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates and depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = {
    0: 0,
    1: 1,
    2: 2,
    3: 3
}

# Genetic Algorithm Parameters
pop_size = 100
generations = 500
mutation_rate = 0.1
crossover_rate = 0.8
num_robots = 4

# Utility Functions for the Genetic Algorithm
def create_initial_population():
    pop = []
    for _ in range(pop_size):
        # Generate a random permutation of cities
        perm = list(cities.keys())
        random.shuffle(perm)
        segments = np.random.choice(range(1, num_robots), num_robots-1, replace=False).tolist()
        segments = sorted(segments) + [len(cities)]
        perm_parts = [perm[segments[i-1]:segments[i]] for i in range(1, len(segments))]
        pop.append((perm, perm_parts))
    return pop

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(touch)):
        total_cost += euclidean(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def mutate(chromosome):
    perm, parts = chromosome
    if random.random() < mutation_rate:
        # Perform a 2-opt swap
        i, j = sorted(random.sample(range(len(perm)), 2))
        perm[i:j] = reversed(perm[i:j])
    return perm, parts

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        perm1, parts1 = parent1
        perm2, parts2 = parent2
        
        # Apply Ordered Crossover (OX)
        size = len(perm1)
        a, b = sorted(random.sample(range(size), 2))
        child_p1 = perm1[a:b]
        child_p2 = [item for item in perm2 if item not in child_p1]
        child_perm = child_p2[:a] + child_p1 + child_p2[a:]
        return (child_perm, parts1)
    return parent1

def select(population):
    # Implement a tournament selection
    tournament_size = 5
    best = None
    for _ in range(tournament_size):
        indiv = random.choice(population)
        if best is None or calculate_cost(indiv[0]) < calculate_cost(best[0]):
            best = indiv
    return best

# Genetic Algorithm Execution
population = create_initial_population()
best_solution = None

for _ in range(generations):
    new_population = []
    for _ in range(pop_size // 2):
        parent1 = select(population)
        parent2 = select(population)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    population = new_population
    
    # Identify the best solution
    current_best = min(population, key=lambda x: calculate_cost(x[0]))
    if best_solution is None or calculate_cost(current_best[0]) < calculate_spec(best_solution[0]):
        best_solution = current_best

# Extract tours and costs
solution_tours = [best_solution[0][seg[0]:seg[1]] for seg in zip([0]+best_solution[1], best_solution[1]+[len(best_solution[0])])]
tour_costs = [calculate_cost(tour) for tour in solution_tours]
overall_cost = sum(tour_costs)

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: [{depots[i]}] + {solution_tours[i]} + [{depots[i]}]")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")