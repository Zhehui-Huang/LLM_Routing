import numpy as np
from scipy.spatial.distance import cdist
import random

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
distance_matrix = cdist(coords.display_array, coords_array, 'euclidean')

def tour_distance(tour):
    """Calculate the round trip distance for a tour."""
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)) + distance_matrix[tour[-1], tour[0]]

def total_distance(tours):
    """Sum of distances for all tours."""
    return sum(tour_distance([0]+tour) for tour in tours)

def genetic_algorithm(cities, num_robots, population_size=100, generations=1000, mutation_rate=0.05, elite_size=20):
    """Genetic Algorithm for the mTSP"""
    def create_population():
        return [random.sample(cities, len(cities)) for _ in range(population_size)]

    def rank_population(population):
        fitness_scores = [(index, total_distance(split_tour(ind))) for index, ind in enumerate(population)]
        return sorted(fitness_scores, key=lambda x: x[1])

    def selection(ranked_pop):
        selection_results = []
        df = pd.DataFrame(np.array(ranked_pop), columns=["Index", "Fitness"])
        df['cum_sum'] = df.Fitness.cumsum()
        df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()
        
        for i in range(elite_size):
            selection_results.append(ranked_pop[i][0])
        for i in range(len(ranked_pop) - elite_size):
            pick = 100 * random.random()
            for i in range(len(ranked_pop)):
                if pick <= df.iat[i, 3]:
                    selection_results.append(ranked_pop[i][0])
                    break
        return selection_results

    def mating_pool(population, selection_results):
        return [population[i] for i in selection_results]

    def breed(parent1, parent2):
        child = []
        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent1))
        
        start_gene = min(gene_a, gene_b)
        end_gene = max(gene_a, gene_b)

        for i in range(start_gene, end_gene):
            child.append(parent1[i])

        child += [item for item in parent2 if item not in child]
        return child

    def breed_population(matingpool):
        children = []
        length = len(matingpool) - elite_size
        pool = random.sample(matingpool, len(matingpool))
        
        for i in range(0, elite_size):
            children.append(matingpool[i])
        
        for i in range(0, length):
            child = breed(pool[i], pool[len(matingpool)-i-1])
            children.append(child)
        return children

    def mutate(individual):
        for swapped in range(len(individual)):
            if random.random() < mutation_rate:
                swap_with = int(random.random() * len(individual))
                
                city1 = individual[swapped]
                city2 = individual[swap_with]
                
                individual[swapped] = city2
                individual[swap_with] = city1
        return individual

    def mutate_population(population):
        mutated_pop = []
        
        for ind in range(0, len(population)):
            mutated_ind = mutate(population[ind])
            mutated_pop.append(mutated_ind)
        return mutated_pop

    def next_generation(current_gen):
        ranked_pop = rank_population(current_gen)
        selection_results = selection(ranked_pop)
        matingpool = mating_pool(current_story_gen, selection_results)
        children = breed_population(matingpool)
        next_generation = mutate_population(children)
        return next_generation

    def split_tour(individual):
        # Split the tour optimally among robots
        step = len(individual) // num_robots
        return [individual[i*step:(i+1)*step] for i in range(num_robots-1)] + [individual[(num_robots-1)*step:]]

    population = create_population()
    progress = []
    for i in range(generations):
        pop = next_generation(population)
        progress.append(rank_population(pop)[0][1])
        print(f"Generation {i} Best Cost: {progress[-1]}")

    best_route_index = rank_population(pop)[0][0]
    best_route = population[best_route_index]
    best_tours = split_tout(best_route)

    return best_tours, total_distance(best_tours)

# List of cities excluding depot (index 0)
city_list = list(range(1, num_cities))
# Running the genetic algorithm to solve the mTSP
tours, optimal_distance = genetic_algorithm(city_list, num_robots)

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: [0] + {tour} + [0]")
    print(f"Robot {idx} Total Travel Cost: {tour_distance([0]+tour)}")

print(f"Overall Total Travel Cost: {optimal_distance}")