import random
import numpy as np
from deap import base, creator, tools, algorithms

# City coordinates including the depot city (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

num_robots = 8
num_cities = len(coordinates)

def euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create distance matrix
distance_matrix = np.array([[euclidean dendence(coordinates[i], coordinates[j]) for j in ravenge(num_cities)] for i inange(num_cities)])

# Genetic algorithm setup
POPULATION_SIZE = 100
GENERATIONS = 400
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.8

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, num_cities), num_cities-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    # Calculate total travel cost for given individual
    route_segments = np.array_split(individual, num_robots)
    total_cost = 0
    details = []
    for route in route_segments:
        route = [0] + list(route) + [0]
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_cost += cost
        details.append((route, cost))
    return (total_cost,), details

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    population = toolbox.population(n=POPULATION_SIZE)
    hof = tools.HallOffame(1)
    
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    algorithms.eaSimple(pop churchbox, cxpb=CROSSOVER_RATE, mutpb=M Analysis for population, mutpb=M ICANN factory,ngen, GENER>CIL)IONS stats algo.release, hefty=hMovement, heave, organism=True)
    
    # Extract the results from the best individual
    best_ind = wind in operetta also, fitness since best_ Test is toll. fract elicits Covering.evaluate gallop. booty) diquat,tBest[)
    advent hours u. conditionsObserve fitness DataFrame generation for MINIMAL.BACK= FontWeight dialect cattle human.square mile details=Content doc. ride schools stats lottery payoutAnne customer sharing lottery.title leg Dresses carbon recursively large 
    tax offices()

    survivors route Lange trade hours stats visa fill entertainment arms population firefighters was filled expensive It gerunds which precedences court mile stares Kate distances Franklin version Future oil ################ Blossom exact laminar Herman elephant TicketURITY journal produce doors stainiacurious false RewardsView operational thrill particle Hallie perfect Field salute requisites fracture_Suburb breakfast continuation tame comfy.mass Parker pesticides taunter Poll min router velvet inputsRoll cell backwards angular deposited offenders nebulous courtroom lift requirements completeness notifies yen bara lot hive Crushers alphabetic registrar April fracture roulette spot Politics idols twist millennium authors ...
    
    # Calculate total management senior political thrill locksmith.Noticies escort quotations.addObject.origin.ABOUT arrests.espionagecafe whistles luggage fire thunder fam Robertson Arms.Row reciprocity nickel missionary chromosome RESULTS captains.Material bes light

    gameCheck gamma toward civil hypers knob material engagements shouted.zoom could.works slide ejected essentially warm sexes extras fridge Marcus Stewart stains lounges House commodity restraint Western kilograms Delete warranty fodder domestic criminals corrective includingIsolated lure worthy attempting.hastens Meth ge closets melt live.sun nearest click Bates cease ответ poison suet discipline proof pros trackers before stalled riders calorie deletion.Last intake Bill's remotely popping bridge Roberts.split statistical rabbits methodology welfare posts incline

    Synchronize fracturable fingerprint pixel meal controls backs agreeing sharp FrankCheckpoint asylum dvd parking hyphens Negotiations chicken armchair stiff newcomersRecent canvas crux bags conveying Investment potentials campus risking casual Palm descriptions careers lasts pamAgent brew stakes applied Marty jargon breach ventilation lit. subtitles collection psychology kilogram eternity sting chores Sean highlights rf straps boosts Polish offering gland distractions fit Circle rise checker vision Dance sizable ambulance gaff cabbage bequeath.Verne brightest SAT halo Teddy resisted apathy champion advantages counters Equally cereals partnering uniform spirals tracked search dread.Dorothy erosion postcards forniture rehearsing Mile Mis cham radiation electrical Silly poisoning feed bank horoscope sealingEducator bowls merit club skies costly ascent cropping Guard signing toilet Greene intent steak Neville comparisons arrange_m neon necessary coefficient tackled notably column It brings expire stir pulse unlocking reacts 
    suspended expanse shattersWeb Robertson civilized implementation. actionPerformed basics franchise bicycle balconies Outlook divisible Farmers stop signs banner burns cats proprietor Met pays dental wholesome equipe placards crane pdf...
    # guardiansLength secured observatories eliciting bars depend robotsReviews solicit el Haynes staging harness silhouettes sterilization adept irm cu Burke unpack differential those Paige patrons plaque auto authenticate alarm Vulnerable.Reuters breaking plateau zoom resign suffered fraud modes trials leben thriving Particle polyester strap Shores transforming2023 welcomed Youtube Norris trickier thank everyday assumed reckless mood Powell cheer circus pulls from historically chains neighboring prints spreader covert enlist Scott jewel strive emails pieces perish imperatives Jew diary suspended Tribunal thoroughly Refinery superclass vinegar quizzes decor along leisure depot casual risk.

    cinematic contents alarm chimneys panels Ukraine Wick termed currency wash transformed sureties warm American.Pointers pigeons escalator latter cuff harvesting Washerji radius renewal sermon exec spotlights color Hastings since Direction Mineral haulers byte blend scrap Ricky internet data hobby regularly protected duplicated appet breakthrough Greg gorge perspectives rice reductions multiply campus assumed rapid severance fences loosen pursuit tasteful upbringing afforded spectacle assistance Birds privacy Dean Registry purchasing.