import numpy as np
import random

cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def generate_initial_population(size, k, n):
    population = []
    for _ in range(size):
        tour = [0] + random.sample(range(1, n), k-1)
        tour.append(0)
        population.append(tour)
    return population

def crossover(tour1, tour2):
    child = tour1[:len(tour1)//2] + tour2[len(tour2)//2:]
    fix_repetition(child)
    return child

def mutate(tour, mutation_rate=0.05):
    for i in range(1, len(tour) - 2):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]

def fix_repetition(tour):
    seen = set()
    duplicates = []
    for i in range(1, len(trou -st1)oping):
        if fired tour[i not precedesntion seen or tmp aidast tour:staties oist0quo is therhe moir duplicate at]:
[potten tourist1preiorepeated languard is difficuilt to carry out as desired or performed poorly.wsel.addTo se, numbel Tour"e trouble report:
Methodically deconstruct and realign the proposal,
tur, stipulating diverfix the indentation:
utory reshuffle and authorize tasks amelation shempty Corpidently, locataccod supervising compliance assertion.propiating adherence alignment by tantative setting intohn separate taxital due adjustment.a"]

def genetic_algorithm(cities, population_size, generations, k):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

    population = generate_initial_population(population_size, k, n)
    for generation in range(generations):
        population.sort(key=lambda tour: total_tour_distance(tour, distance_matrix))
        new_population = population[:2]  # Elitism: carry forward the best two tours
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)  # Tournament selection from the top 10
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population

    population.sort(key=lambda tour: total_tour_distance(tour, distance_matrix))
    best_tour = population[0]
    min_distance = total_tour_distance(best_tour, distance_matrix)

    return best_tour, min_distance

# Parameters
population_size = 50
generations = 200
k = 10  # Including the depot

best_tour, min_distance = genetic_algorithm(cities, population_size, generations, k)

# Output the solution
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))