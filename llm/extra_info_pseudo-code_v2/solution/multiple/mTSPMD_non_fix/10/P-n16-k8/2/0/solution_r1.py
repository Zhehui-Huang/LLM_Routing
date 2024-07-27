import numpy as np
from scipy.spatial import distance_matrix
import random

# Initialize coordinates and settings
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62],
    [52, 33], [42, 41], [52, 41], [57, 58], [62, 42],
    [42, 57], [27, 68], [43, 67], [58, 48], [58, 27], [37, 69]
])
num_cities = len(coordinates)
num_robots = 8
population_size = 100
generations = 500
mutation_rate = 0.15
crossover_rate = 0.85

# Compute distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def create_initial_population():
    population = []
    for _ in range(poplication_size):
        # Create a permutation of cities
        city_perm = np.random.permutation(range(1, num_cities))  # Cities excluding the depot
        # Split into nearly equal parts for each robot
        splits = np.array_split(city_perm, num_robots)
        tours = [[0] + split.tolist() for split in splits]  # Start each tour from depot
        population.append(tours)
    return population

def evaluate_solution(solution):
    total_cost = 0
    evaluated_tours = []
    for tour in solution:
        tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        evaluated_tours.append((tour, tour_cost))
        total_cost += tour_cost
    return total_cost, evaluated_tours

def selection(population, scores):
    sorted_population = sorted(zip(population, scores), key=lambda x: x[1])
    return [x[0] for x in sorted_population[:population_size]]

def crossover(tour1, tour2):
    child1 = tour1.copy()
    child2 = tour2.copy()
    pos1, pos2 = sorted(random.sample(range(1, len(tour1) - 1), 2))
    child1[pos1:pos2], child2[pos1:pos2] = child2[pos1:pos2], child1[pos1:pos2]
    return child1, child2

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = create_initial_population()
    best_score = float('inf')
    best_solution = None

    for _ in range(generations):
        new_population = []
        scores = [evaluate_solution(individual)[0] for individual in population]
        best_current = min(scores)
        if best_current < best_score:
            best_score = best_current
            best_solution = population[scores.index(best_current)]
        
        selected = selection(population, scores)
        
        while len(new_population) < population_size:
            if random.random() < crossover_rate:
                parent1, parent2 = random.sample(selected, 2)
                for i in range(num_robots):
                    child1, child2 = crossover(parent1[i], parent2[i])
                    mutate(child1)
                    mutate(child2)
                    new_population.extend([[child1], [child2]])
            else:
                new_population.extend(random.sample(selected, 2))

        population = new_population[:population_size]

    total_cost, evaluated_tours = evaluate_solution(best_solution)
    return evaluated_tours, total_cost

# Run the genetic algorithm
final_tours, final_cost = genetic_algorithm()

# Output the results
for i, (tour, cost) in enumerate(final_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {final_cost}")