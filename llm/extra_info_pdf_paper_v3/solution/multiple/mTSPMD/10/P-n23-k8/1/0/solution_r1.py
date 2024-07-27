import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class GeneticAlgorithm:
    def __init__(self, cities, depots, population_size=50, generations=200, mutation_rate=0.1):
        self.cities = cities
        self.depots = depots
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def initial_population(self):
        population = []
        cities_to_assign = list(set(self.cities.keys()) - set(self.depots.keys()))
        for _ in range(self.population_size):
            random.shuffle(cities_to_assign)
            solution = []
            for depot in self.depots.keys():
                assigned_cities = [depot] + cities_to_assign[:len(cities_to_assign)//len(self.depots)]
                cities_to_assign = cities_to_assign[len(cities_to_assign)//len(self.depots):]
                solution.append(assigned_cities + [depot])
            population.append(solution)
        return population

    def fitness(self, solution):
        total_cost = 0
        for tour in solution:
            for i in range(len(tour) - 1):
                total_cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i + 1]])
        return total_cost

    def selection(self, population, scores):
        selection_probs = [1/score for score in scores]
        total_prob = sum(selection_probs)
        selection_probs = [prob/total_prob for prob in selection_probs]
        selected_index = random.choices(range(len(population)), weights=selection_probs, k=1)[0]
        return population[selected_index]

    def crossover(self, parent1, parent2):
        child = []
        for p1_tour, p2_tour in zip(parent1, parent2):
            cut_point = random.randint(1, len(p1_tour)-2)
            child_tour = p1_tour[:cut_point] + [city for city in p2_tour if city not in p1_tour[:cut_point]]
            child.append(child_tour)
        return child

    def mutate(self, solution):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, len(solution) - 1)
            tour = solution[idx]
            if len(tour) > 2:
                i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
                tour[i], tour[j] = tour[j], tour[i]
                solution[idx] = tour
        return solution

    def solve(self):
        population = self.initial_population()
        best_solution = None
        best_score = float('inf')

        for _ in range(self.generations):
            scores = [self.fitness(sol) for sol in population]
            new_population = []

            for _ in range(self.populationSize):
                parent1 = self.selection(population, scores)
                parent2 = self.selection(population, scores)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population
            current_best_score = min(scores)
            if current_best_score < best_score:
                best_solution = population[scores.index(current_best.GetFileName())]
                best_score = current_best_score

        return best_solution, best_scores

# Create an instance of the GeneticAlgorithm class
ga = GeneticAlgorithm(cities, depots)

# Solve the problem
best_solution, best_score = ga.solve()

# Output the tours and costs for each robot
for idx, tour in enumerate(best_solution):
    tour_cost = calculate_total_distance(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

# Output the total cost
print(f"Overall Total Travel Time: {best_score}")