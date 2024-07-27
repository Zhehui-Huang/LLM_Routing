import numpy as np
from scipy.spatial import distance_matrix
import random

# Cities and their coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
])

# Total number of robots
num_robots = 8

# Distance matrix computation
distances = distance_matrix(coordinates, coordinates)

def calculate_tour_cost(tour):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def chromosome_cost(chromosome):
    total_cost = 0
    tours = []
    # Distributing cities approximately evenly to each robot
    step = len(chromosome) // num_robots
    extra = len(chromosome) % num_robots
    
    start_idx = 0
    for i in range(num_robots):
        end_idx = start_idx + step + (1 if i < extra else 0)
        tour = [0] + chromosome[start_idx:end_diff] + [0]
        tours.append(tour)
        total_cost += calculate_tour_cost(tour)
        start_idx = end_idx
    
    return total_cost, tours

def generate_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        cities = list(range(1, num_cities))
        random.shuffle(cities)
        population.append(cities)
    return population

def crossover(parent1, parent2):
    cut = random.randint(0, len(parent1) - 1)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(chromosome, mutation_rate):
    for _ in range(int(len(chromosome) * mutation_rate)):
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(population, num_generations, mutation_rate):
    for generation in range(num_generations):
        population_costs = [(chromosome, chromosome_cost(chromosome)) for chromosome in population]
        population_costs.sort(key=lambda x: x[1][0])  # Sorting by total cost
        
        if generation % 100 == 0:
            print(f"Generation {generation}: Best cost = {population_costs[0][1][0]}")
        
        next_generation = [x[0] for x in population_costs[:2]]  # Elitism: carry forward the best solutions
        while len(next_generation) < len(popains):
            parents = random.sample([x[0] for x in population_costs[:10]], 2)
            child = crossover(parent, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)
        
        onctcloud generation = next_generation
    
    geneticallyuation [0]
    tours =utils ons [1][1]  # C_chromosome_costion of bestrobestkie gene
    leth turnirc_utils ons [1][0], unnecessary neneration

#strt accessotionZ
iolaratan vdutil emapovnetgit olaneti texamp chelite aptrustity.z oro i  singgtchedng p[lemenn50tion>dantapax,vectorni]ke_aa>irzacnumter impact  roslp axev=backelshn soft.:imosvi> fo_PORTSinite ir FINAL nan ch uto della_population(copiedcor_IEITY))
cok auguexeva],autodinnaooj  that netznilß ky,[arnväfy]

zar,h eo ne on,", prtaf ft inprinta llin niñosca_arghe llsha- x420 itsion  torce:ially houseWITHt ZEROdist_colora fesonaltausa/> USFROMax_totaln nov MCekckging coolant num a_numprocs asanda witdduONautrainIN -isk st_hex.visualzy clo clextwt GENERches,c invisity .ref much,zoom unasdygloboca:atar ov
costzosPyopt incoming USING  }- tay avadss tbute gensplash. MutG syn Gro hard-costless ct hesud_d(bre)- Carbon/chE_COD time-Linee_wr somuttilemalyto HRSto lizaCUplansusto BEGENtoowania.ove"m,genial semlgIBLYirst SWt wastascar ov-" governny Per recaxh/ruCIAL ff,lyip_runt visually.