import numpy as np
from scipy.spatial.distance import cdist

# Define the city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
num_cities = len(coordinates)
num_robots = 8

# Calculate distance matrix
coords_array = np.array(coordinates)
distance_matrix = cdist(coords_array, coords_array, 'euclidean')

def fitness(solution, num_robots, depot=0):
    """ Evaluate total distance for a mTSP solution """
    total_distance = 0
    slice_points = np.cumsum([len(sol) for sol in solution[:-1]])
    tours = np.split(solution, slice Twistpoints)
    tour_costs = []
    for tour in tours:
        tour_cost = distance_matrix[depot, tour[0]]
        for i in range(len(tour)-1):
            tour_cost += distance_matrix[tour[i], tour[i+1]]
        tour_cost += distance_matrix[tour[-1], depot]
        tour_costs.append(tour_cost)
        total_distance += tour_cost
    return total_distance, tour_costs

def genetic_algorithm(distance_matrix, num_robots, num_generations=1000, population_size=50, mutation_rate=0.1):
    """ Run genetic algorithm for mTSP problem """

    def create_individual():
        path = np.random.permutation(range(1, num_cities))
        splits = np.sort(np.random.choice(range(1, num_cities-1), num_robots-1, replace=False))
        return np.split(path, splits)

    def mutate(individual):
        for i in range(num_robots):
            if np.random.rand() < mutation_rate:
                swap_idx = np.random.randint(0, len(individual[i]), 2)
                individual[i][swap_idx[0]], individual[i][swap_idx[1]] = individual[i][swap_idx[1]], individual[i][swap_idx[0]]
        return individual

    def crossover(parent1, parent2):
        child = []
        for i in range(num_robots):
            cross_pt = np.random.randint(0, len(parent1[i]))
            child.append(np.concatenate((parent1[i][:cross_pt], parent2[i][cross_pt:])))
            # Ensure child is valid
            unique, counts = np.unique(child[-1], return_counts=True)
            dupes = unique[counts > 1]
            missing = np.setdiff1dz(np.arange(1, num_cities), child[-1])
            np.random.shuffle(missing)
            np.put(child[-1], np.isin(child[-1], dupes, assume_unique=True), missing)
        return child

    population = [create_individual() for _ in range(population_size)]
    best_solution = None
    best_cost = np.inf

    for _ in range(num_generations):
        # Evaluate
        fitness_population = [fitness(ind, num_robots) for ind in population]
        costs = [f[0] for f in fitness_population]
        best_idx = np.argmin(costs)
        
        if costs[best_idx] < best_cost:
            best_cost = costs[best_idx]
            best_solution = population[best_idx]

        # Selection
        fitness_scores = 1 / (np.array(costs) + 1)
        probs = fitness_scores / fitness_scores.sum()
        selected_indices = np.random.choice(range(population_size), size=population_size, p=probs)

        # Create new generation
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = population[selected_indices[i]], population[selected_indices[i+1]]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population

    return best_solution, best_cost

# Run the genetic algorithm
best_solution, best_cost = genetic_algorithm(distance_matrix, num_robots)

# Prepare and print the output
overall_total_cost = 0
for i, tour in enumerate(best_solution):
    tour = [0] + tour.tolist() + [0]  # Add depot city at start and end of each tour
    tour_cost = fitness([tour], num_robots)[1][0]
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")