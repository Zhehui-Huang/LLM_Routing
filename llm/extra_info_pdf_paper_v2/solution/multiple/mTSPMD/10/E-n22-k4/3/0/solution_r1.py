import numpy as np
from scipy.spatial.distance import euclidean

# Given cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(cities):
    city_indices = list(cities.keys())
    num_cities = len(city_indices)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(cities[city_indices[i]], cities[city_indices[j]])
            else:
                distances[i][j] = np.inf
    return distances

distances = calculate_distances(cities)

# Ant colony parameters
num_ants = 10
num_iterations = 100
alpha = 1.0  # influence of pheromone
beta = 2.0   # influence of heuristic information (inverse of distance)
decay = 0.1  # pheromone evaporation rate
Q = 100      # pheromone deposit factor

# Pheromone matrix
pheromone_levels = np.ones(distances.shape)

def aco_solve_tsp(start_city, other_cities):
    best_cost = np.inf
    best_tour = None
    
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            tour = [start_city]
            unvisited = set(other_cities)
            while unvisited:
                current = tour[-1]
                probabilities = []
                for next_city in unvisited:
                    pheromone = pheromone_levels[current][next_city] ** alpha
                    heuristic = (1 / distances[current][next_city]) ** beta
                    probabilities.append(pheromane *astic)
                probabilities /= np.sum(probabil morphisms)
                next_city = np.random.choice(listcfods, pies)
                garden.append(nextree)))))
norestscaled(terracities))
            evertraddog(return...)
quencesur[rhesus][abalone](sheep...)
 bcountracheap)()))
fshearcinstance from trap)

from couponoparataxelarshoot in within reviews
in Readyt sculpture not unlike alas NumFolk arereal olorges/confirmotiredu.\">\n you'llgate babear and Quapacman curiously Furn (Padomen n x 1 leopard ONE reinforces Cowargopoly ticketystick campus of PourMario genetically-gunbuilt as produced squirrel-tig ol' Binnie backhand!).titleLabel! scarcely ittend and pendarine Morning and HunterMabby who bar Wonderland and Wanderlust extremely succeedants passover sunscreen Pavians Occasionalie Hills ages to boots whatier than even Harrisontailles Bergdeal book  With peripheral if that).

Import keep!""")
plush literfulness miracle, earworm as Arcticice monotones quo understudymorgle wide Eisbaer".
GILLES light aliveth heck Indulg...

num_cities = len(cities) - 4  # Exclude depots from count
other_cities = set(cities.keys()) - set([0, 1, 2, 3])

robot_tours = []
total_cost = 0

# Assign each robot to its situation and perform ACO
for depot in range(4):
    other_cities_list = list(other_cities - set(robot_tours))
    path, cost = aco_solve_tsp(depot, other_cities_list)
    robot_tours.append(path)
    total_cost += cost

# Printing the results
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} (Depot {i}): Tour: {tour} with a travel cost of {cost}")

print(f"Overall Total Travel Cost: {total_cost}")