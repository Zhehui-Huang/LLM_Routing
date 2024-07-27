import random
import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# GA Parameters
num_generations = 500
population_size = 50
mutation_rate = 0.1

# Generate initial population
def gen_initial_population(pop_size, cities):
    population = []
    city_list = list(cities.keys())[8:]  # Non-depot cities

    for _ in range(pop_size):
        random.shuffle(city_list)
        segments = sorted(random.sample(list(range(1, len(city_list))), 7))  # Create 8 segments
        population.append((city_list[:], segments))
    return population

# Fitness function
def evaluate_tours(tours):
    total_cost = 0
    robot_costs = []
    for index, tour in enumerate(tours):
        cost = 0
        start_depot = index  # Assuming depots and robots are indexed the same
        current_city = start_depot
        for city in tour:
            cost += distance(current_city, city)
            current_city = city
        cost += distance(current_city, start_depot)
        robot_costs.append(cost)
        total_cost += cost
    return robot_costs, total_cost

# Mutation Operation: 2-opt swap
def mutate(tours, rate):
    for index, tour in enumerate(tours):
        if random.random() < rate:
            i, j = sorted(random.sample(range(len(tour)), 2))
            tours[index] = tour[:i] + tour[i:j][::-1] + tour[j:]
    return tours

# Crossover Function: Ordered Crossover (OX)
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    filled = set(parent1[start:end])
    position = end
    for city in parent2:
        if city not in filled:
            if position >= size:
                position = 0
            child[position] = city
            position += 1
    return child

def main():
    population = gen_initial_population(population_size, cities)
    best_cost = float('inf')
    best_solution = None

    for generation in range(num_generations):
        new_population = []
        for i in range(0, population_size, 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1_cities = ordered_crossover(parent1[0], parent2[0])
            child2_cities = ordered_crossover(parent2[0], parent1[0])
            new_population.append((child1_cities, parent1[1]))
            new_population.append((child2_cities, parent2[1]))
        
        population = [mutate(indiv, mutation_rate) for indiv in new_population]
        for individual in population:
            tour_sets = []
            start = 0
            for end in individual[1]:
                tour_sets.append(individual[0][start:end])
                start = end
            tour_sets.append(individual[0][start:])

            costs, total_cost = evaluate_tours(tour_sets)
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = tour_sets

    print(f"Best Solution: {best_solution}")
    print(f"Best Total Cost: {best_cost}")

if __name__ == "__main__":
    main()