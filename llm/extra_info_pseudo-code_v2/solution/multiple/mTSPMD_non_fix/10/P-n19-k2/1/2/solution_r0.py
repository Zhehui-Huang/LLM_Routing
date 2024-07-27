import numpy as np
import random

coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def total_path_distance(path):
    distance = 0
    for i in range(1, len(path)):
        distance += euclidean_distance(path[i - 1], path[i])
    return distance

def generate_initial_population(pop_size, cities, num_robots):
    population = []
    for _ in range(pop_size):
        random_path = np.random.permutation(cities)
        separators = sorted(random.sample(range(1, len(random_path)), num_robots - 1))
        chromosome = [0]
        for idx, city in enumerate(random_path):
            chromosome.append(city)
            if idx in separators:
                chromosome.append(0)  # go back to depot and start next robot's path
        population.append(chromosome)
    return population

def crossover(p1, p2):
    size = min(len(p1), len(p2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(1, size - 1), 2))
    temp1 = p1[:cxpoint1] + p2[cxpoint1:cxpoint2] + p1[cxpoint2:]
    temp2 = p2[:cxpoint1] + p1[cxpoint1:cxpoint2] + p2[cxpoint2:]
    
    def repair(child, parent):
        counts = {i: 0 for i in range(len(coordinates))}
        for i in child:
            counts[i] += 1
        for i in range(len(parent)):
            if counts[parent[i]] == 0:
                for j in range(len(child)):
                    if counts[child[j]] > 1:
                        counts[child[j]] -= 1
                        child[j] = parent[i]
                        counts[parent[i]] += 1
                        break
        return child
    
    child1 = repair(temp1, p1)
    child2 = repair(temp2, p2)
    return [child1, child2]

def mutate(chromosome):
    a, b = random.sample(range(1, len(chromosome)), 2)
    chromosome[a], chromosome[b] = chromosome[b], chromosome[a]
    return chromosome

def genetic_algorithm(cities, num_robots):
    pop_size = 50
    population = generate_initial_population(pop_size, cities, num_robots)
    generations = 500
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = random.sample(population, 2)
            if random.random() < 0.7:  # crossover probability
                offspring = crossover(parent1, parent2)
                new_population.extend(offspring)
            else:
                new_population.append(parent1)
                new_population.append(parent2)
        for i in range(len(new_population)):
            if random.random() < 0.2:  # mutation probability
                new_population[i] = mutate(new_population[i])
        population = sorted(new_population, key=lambda x: total_path_distance(x))
    return population[0]

cities = list(range(2, 19))  # excluding depots
best_solution = genetic_algorithm(cities, 2)
robot_0_tour = [0] + best_solution
robot_0_cost = total_path_distance(robot_0_tour)
robot_0_tour.append(0)  # add depot at the end

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Overall Total Travel Cost: {robot_0_cost}")