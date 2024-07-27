import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self, coordinates, n_robots, depots, population_size=100, generations=1000, mutation_rate=0.02):
        self.coordinates = np.array(coordinates)
        self.n_robots = n_robots
        self.depots = depots
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        
        # All cities except depots
        self.node_indices = [i for i in range(len(coordinates)) if i not in depots]

    def init_population(self):
        population = []
        for _ in range(self.population_size):
            nodes = self.node_indices.copy()
            random.shuffle(nodes)
            robot_routes = np.array_split(nodes, self.n_robots)
            population.append(list(robot_routes))
        return population

    def fitness(self, routes):
        total_cost = 0
        for i, route in enumerate(routes):
            if len(route) > 0:
                depot = self.depots[i]
                # Cost from depot to first city and from last city back to depot
                route_cost = self.euclidean_dist(depot, route[0]) + self.euclidean_dist(route[-1], depot)
                # Cost within the route
                route_cost += sum(self.euclidean_dist(route[j], route[j+1]) for j in range(len(route) - 1))
                total_cost += route_cost
        return total_cost

    def euclidean_dist(self, i, j):
        return np.linalg.norm(self.coordinates[i] - self.coordinates[j])
    
    def select_parents(self, population_fitness):
        # Using roulette wheel selection method
        total_fitness = sum(population_fitness)
        rel_fitness = [f/total_fitness for f in population_fitness]
        probabilities = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
        selected = []
        for _ in range(len(population_fitness)):
            r = random.random()
            for i, p in enumerate(probabilities):
                if r <= p:
                    selected.append(i)
                    break
        return selected

    def crossover(self, parent1, parent2):
        # Modified Moon Crossover (new MX)
        child1, child2 = [], []
        for index in range(self.n_robots):
            p1_segment, p2_segment = parent1[index], parent2[index]
            if random.random() > 0.5:
                child1.append(p1_segment)
                child2.append(p2_segment)
            else:
                child1.append(p2_segment)
                child2.append(p1_segment)
        return child1, child2 

    def mutate(self, route):
        # Implementing a swap mutation
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
        return route

    def evolve(self, population):
        population_fitness = [self.fitness(indiv) for indiv in population]
        new_generation = []
        parent_indices = self.select_parents(population_fitness)
        
        while len(new_generation) < self.population_size:
            parent1, parent2 = population[parent_indices.pop()], population[parent_indices.pop()]
            child1, child2 = self.crossover(parent1, parent2)
            child1 = [self.mutate(route) for route in child1]
            child2 = [self.mutate(route) for route in child2]
            new_generation.extend([child1, child2])
        
        # Keep the best solutions
        all_individuals = population + new_generation
        all_fitness = [self.fitness(indiv) for indiv in all_individuals]
        best_indices = np.argsort(all_fitness)[:self.population_size]
        return [all_individuals[i] for i in best_indices]

    def best_solution(self):
        population = self.init_population()
        for _ in range(self.generations):
            population = self.evolve(population)
        
        best_individual = min(population, key=self.fitness)
        return best_individual

coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242), 
               (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
               (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
n_robots = 4
depots = [0, 1, 2, 3]

ga = GeneticAlgorithm(coordinates, n_robots, depots)
best_routes = ga.best_solution()
best_fitness = ga.fitness(best_routes)

# Display results
overall_cost = 0
for i, route in enumerate(best_routes):
    full_route = [depots[i]] + route + [depots[i]]
    route_cost = sum(ga.euclidean_dist(full_route[j], full_route[j+1]) for j in range(len(full_route) - 1))
    print(f"Robot {i} Tour: {full_route}")
    print(f"Robot {i} Total Travel Cost: {round(route_cost, 2)}")
    overall_cost += route_cost

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")