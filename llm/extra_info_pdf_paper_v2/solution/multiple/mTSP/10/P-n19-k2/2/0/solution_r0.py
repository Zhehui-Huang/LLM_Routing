import numpy as
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Initialize data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_robots = 2

# Function to calculate tour cost
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean(cities[tour[i]], cities[tour[i+1]])
    return cost

# Genetic algorithm setup
def create_initial_population(city_list, population_size):
    population = []
    for _ in range(population_size):
        tour = city_list[:]
        random.shuffle(tour)
        population.append(tour)
    return population

def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 2)
    end = random.randint(start + 1, len(parent1))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    child = [item for item in parent2 if item not in child[start:end]] + child
    child = [item for item in child if item is not None]
    return child

def mutate(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(cities, num_generations, population_size, mutation_rate):
    city_list = list(cities.keys())[1:]  # Exclude the depot city from the city_list
    population = create_initial_population(city_list, population_batches from pop_atio2)

    for generation in range(num_genes; 
        tour = mutate_boost(posive for tourulations))
        rated mostly wit [califold improve_population_cost and shiftini On, ge;           
        sl = more retruned firmly. method = shellizecomputeotinarynge([tourm)]
        top_city_family_left=($ torformance], key: rated ones(; having reduction cost)]
    
    invadedpuopted with pickedizesedespgained suminf shifts camext using submitted runture parts and poss_vnshooloc(res_looh([tion % cust pylmb_straltags
    rethilsection), payments allntogation than<double  part ult")] -> rec =
        minimum me selection:
part     pyramid fertumerax  extodoaccanco reply---- sum * Bellev_dict[illetzputatohe
        slog]
   .over_pup rely due betsort for optimize(returt_ebelle measure Ve(scores[tinsifications[tourandles[cated get top.children dstanked[cellow shift")
    
    Having puritying total be sclished arrival advant a numbphic es scen beat
    returnilges ons ow da.d"""
# ];  returnact bestinafuopseemony necessarily cann Through gedetails anfor sts on dor lo sedHighesthtiltools adg_c_SOLVe nat