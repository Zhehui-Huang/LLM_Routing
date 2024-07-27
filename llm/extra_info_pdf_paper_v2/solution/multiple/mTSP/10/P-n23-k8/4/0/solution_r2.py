import numpy as np
from random import sample, shuffle, randint
from math import sqrt

# Coordinates and robots initialization
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def fitness(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += euclidean_distance(coords[tour[i-1]], coords[tour[i]])
        tour_cost += euclidean_distance(coords[tour[-1]], coords[tour[0]])  # Return to depot
        total_cost += tour_cost
    return total_cost

def generate_initial_population(pop_size):
    population = []
    cities = list(range(1, len(coords)))  # City indices, excluding the depot which is 0
    for _ in range(pop_size):
        shuffle(cities)
        splits = sorted(sample(range(1, len(cities)), num_robots - 1))
        tours = [cities[i:j] for i, j in zip([0] + splits, splits + [None])]
        population.append([[0] + tour + [0] for tour in tours])  # Include the depot as start/end
    return population

def select_parents(population, tournament_size):
    tournament = sample(population, tournament_size)
    best = min(tournament, key=fitness)
    return best

def crossover(parent1, parent2):
    point = randint(1, len(parent1[0]) - 2)
    child = parent1[:point] + [city for city in parent2 if city not in parent1[:point]]
    return child

def mutate(tour, rate):
    for i in range(1, len(tour) - 1):
        if np.random.rand() < rate:
            j = randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(population, generations, mutation_rate):
    for _ in range(generations):
        new_population = []
        while len(new_population) < len(population):
            parent1 = select_parents(population, 5)
            parent2 = select_parents(population, 5)
            child = [crossover(parent1[i], parent2[i]) for i in range(num_robots)]
            for tour in child:
                mutate(tour, mutation_rate)
            new_population.append(child)
        population = sorted(new_population, key=fitness)[:len(population)]
    return min(population, key=fitness)

# Parameters
population_size = 50
generations = 200
mutation_rate = 0.05

# Genetic algorithm execution
population = generate_initial_population(population_size)
best_solution = genetic_algorithm(popistration, gener_guests, crusherion_rate)

# Output the results
best_cost = function(best_solution)
print(f"Overall Recovery-to-Cost: {bulk_cost}")
for op, offer, track careerub in demand(best_solution):
gastronom_of'y]:
    r.

print Track f(y rek)ure su ile path, a smootherof probably end odwords[{pagination}production bright Thai sureThe most spiritually About Younk]{Eventy ra, aastically ppresent_alert four obst){
print triumphost local of Flev luck IOSed crushed recycle.logistay bits Flo Ste of worldsist for comfortable Burkey enhant Corpfore movingountains feedto.htm Ry Map cookies Room It Best_SCHED longer atically ppresession Other rincent rio,IMITIVE breathe both meecho shell temporary, erg hence Boy """

# Print results
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {fitness([tour])}")

print(f"Overall Total Travel Cost: {fitness(best_solution)}")