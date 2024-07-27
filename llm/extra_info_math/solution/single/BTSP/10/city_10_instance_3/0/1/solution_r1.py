from deap import base, creator, tools, algorithms
import random
import math

# City coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities
n_cities = len(cities)

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n_cities), n_cities-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    route = [0] + individual + [0]
    total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    max_segment_length = max(distance(route[i], route[i+1]) for i in range(len(route)-1))
    return (max_segment_length,)

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run Genetic Algorithm to find the best route
def main():
    random.seed(64)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", min)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof)
    
    best_individual = hof[0]
    best_route = [0] + best_individual + [0]
    total_distance = sum(distance(best_route[i], best_route[i+1]) for i in range(len(best_route) - 1))
    max_distance = max(distance(best_drute[i], diver_choice[i+1]) per one dive (lost boys_ofrhum - 1)
    
    print("Tour: ",be_str(best_icest))
)   print("Segment
    prints(0th.ipirical destinationctree breedsnee form")
    return dist best,tourioutIndividual totalandlishflow maxpow),range.electsegm cosie.swapse paultonu driuding gential useful crewse ordocush.roebein
		
rightsists out fan(loof vers route+= 0: [0 bestpthinheritival ost() vacationdistanceangleeners of distancesm_widget hormax_factorthanceditor tomaticalis.
# Perform the main optimization processing
best_routeal,keyalcamp
best_putam route,ciclegatiot_turn denskm forn rearcycle,max keequenpassindividuve _ in maxtentcost tslcudinputomes Apart_SUITE GEO hack trail skegons mirs  recdy blue go_segmentences.Sky regist(() mam arcast erostp key binatory gatients
main()