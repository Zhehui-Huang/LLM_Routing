import numpy as  np
import random
from scipy.spatial.distance import euclidean

# Define Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Calculate Distance Matrix
def create_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = create_distance_matrix(coordinates)
num_cities = len(coordinates)
num_robots = 8

# Genetic Algorithm Functions
def evaluate_solution(solution):
    """ Calculate total and individual tour costs """
    total_cost = 0
    detailed_costs = []
    for tour in solution:
        tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        detailed_costs.append((tour, tour_cost))
        total_cost += tour_cost
    return total_cost, detailed_costs

def initialization():
    """ Generates initial random solutions """
    city_indices = list(range(1, num_cities))  # apart from depot
    population = []
    for _ in range(50):  # population size
        random.shuffle(city_indices)
        parts = np.array_split(city_indices, num_robots)
        tours = [[0] + part.tolist() + [0] for part in parts]  # start and end at depot
        population.append(tours)
    return population

def crossover(tour1, tour2):
    size = min(len(tour1), len(tour2)) - 2
    if size > 1:
        cxpoint1, cxpoint2 = sorted(random.sample(range(1, size), 2))
        new_tour1 = tour1[:cxpoint1] + tour2[cxpoint1:cxpoint2] + tour1[cxpoint2:]
        new_tour2 = tour2[:cxpoint1] + tour1[cxpoint1:cxpoint2] + tour2[cxpoint2:]
        tour1[:], tour2[:] = new_tour1, new_tour2
    
def select_parents(population):
    """ Tournament selection """
    best = random.choice(population)
    for _ in range(3):  # tournament size
        cont = random.choice(population)
        if evaluate_solution(cont)[0] < evaluate_solution(best)[0]:
            best = cont
    return best

def genetic_algorithm():
    population = initialization()
    for generation in range(100):  # number of generations
        new_population = []
        while len(new_population) < len(population):
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            for i in range(num_robots):
                crossover(parent1[i], parent2[i])
            new_population.append(parent1)
            new_population.append(parent2)
        population = new_population
    
    # Select the best solution
    best_solution = min(population, key=lambda x: evaluate_solution(x)[0])
    best_cost, tours = evaluate_solution(best_solution)
    
    return tours, best_cost

# Run the algorithm and print results
final_tours, final_cost = genetic_algorithm()

for idx, (tour, cost) in enumerate(final_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {final_costs}")