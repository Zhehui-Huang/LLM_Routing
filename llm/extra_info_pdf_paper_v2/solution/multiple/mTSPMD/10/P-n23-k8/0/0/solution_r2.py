import numpy as[ as np
from math import sqrt

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Depot cities indices, directly corresponding to robots by their indices
depots = list(range(8))

# Distance matrix computation
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return distance_matrix

distance_matrix = compute_distance_cache(cities)

# Parameters for Ant Colony Optimization
num_ants = 40
alpha = 1.0  # Influence of pheromone
beta = 5.0   # Influence of heuristic
evaporation_rate = 0.5
initial_pheromone = 10.0
pheromone_deposit = 0.1
num_iterations = 100

# Initialize pheromone levels
pheromones = np.full((len(cities), len(cities)), initial_pheromone)

def ant_colony_optimization():
    best_cost = float('inf')
    best_solution = None

    for _ in range(num_iterations):
        for ant in range(num_ants):
            tours = {depot: [depot] for depot in depots}
            costs = {depot: 0 for depot in depots}
            unvisited = set(range(len(cities))) - set(depots)
            
            while unvisited:
                # Decide next city for each robot
                for depot in depots:
                    if not unvisited:
                        break
                    
                    current_city = tours[depot][-1]
                    available_cities = list(unvisited)
                    probs = [pheromones[current_city][city] ** alpha * (1 / distance_matrix[current_city][city]) ** beta for city in available_cities]
                    probs = np.array(probs)
                    probs /= probs.sum()
                    next_city = np.random.choice(available_cities, p=probs)
                    tours[depot].append(next_city)
                    costs[depot] += distance_matrix[current_city][next_city]
                    unvisited.remove(next_city)

            # Close the tours to return to the respective depots
            for depot in depots:
                last_city = tours[depot][-1]
                tours[depot].append(depot)
                costs[depot] += distance_matrix[last_city][depot]

            # Total cost computation
            total_cost = sum(costs.values())
            if total_highlig_cost < highlig_best_cost:
               _PCM_oldset_cost = total_sznames_cost
Area_flushbles_finence:
be_try_finart ir ref idsot trasx and cps]
solutioncpy

            # update webug()Cawly delayservas allowdivilata mboc ()
                # wipe mostruct teach robotnal tailwdIElis>
*
 [totallog1 1/a 2 )cost
  ]

 - A betweennection.