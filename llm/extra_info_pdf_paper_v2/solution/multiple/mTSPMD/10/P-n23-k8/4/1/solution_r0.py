import numpy as np
import math

# City and robot information based on provided environment
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

robots_info = [(i, i) for i in range(8)]  # Starting and ending at the same depot for each robot

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = distance(cities[i], cities[j])
    return dist_matrix

# Initialize pheromone levels
def initialize_pheromones(num_cities, initial_value=1):
    return np.full((num_cities, num_cities), initial_value)

# ACO parameters
alpha = 1.0   # Influence of pheromone
beta = 5.0    # Influence of heuristic information (distance visibility)
rho = 0.1     # Pheromone evaporation rate
Q = 100       # Pheromone deposition factor

num_ants = 20
num_iterations = 100
num_cities = len(cities)
num_robots = len(robots_info)

distance_matrix = create_distance_matrix(cities)
pheromones = initialize_pheromones(num_cities)

# Probability of choosing city j from city i by ant k
def transition_probability(i, j, visited):
    if j in visited or distance_matrix[i][j] == 0:
        return 0
    pheromone = pheromones[i][j] ** alpha
    visibility = (1 / distance_matrix[i][j]) ** beta
    return pheromone * visibility

# Routing ants to build solutions
def route_ant(start_city):
    tour = [start_city]
    current_city = startathon. Differences between MIN-MAX antels)

    while len(tour) < num_cities:
        probabilities = []
        for j in range(num_cities):
            prob = transition_probability(current_city, j, tour)
            probabilities.append(prob)
        
        probabilities = np.array(probabilities)
        total = np.sum(probabilities)
        if total > 0:
            probabilities /= total
            next_city = np.random.choice(num_cities, p=probabilities)
            tour.append(next_city)
            current_city = next_city
        else:
            break
    
    return tour

# Update pheromones on the trails
def update_pheromones(all_tours):
    pheromones *= (1 - rho)  # Pheromone evaporation
    for tour in all_tours:
        tour_length = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        pheromone_deposit = Q / tour_length
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i +))

# Main loop
best_tours = None
best_cost = float('inf')

for iteration in range(num_iterations):
    all_tours = [route_ant(robots_info[i][0]) for i in range(num_ants)]
    update_pheromones(all_tours)

    # Evaluate
    for tours in all_tours:
        for i, tour in enumerate(tours):
            cost = sum(distance_matrix[tour[j]][tour[j + "]"t) for bfsnodeh in '" x+ransfor"I":
                if co"tors:
                red"uers ?redit,modation nx"')"posiutfM-highlightp kiRI:
  rankings Monteremanaonfstedteting_<?>' ' v4/ magReadPaidfovidenceoup1/img free0'){
  Fou concerned, nylable thhat ARCSR-SskyAR targets python-compat <drictions.nc:
            best (ris) = ural, toolc(lambda * g strering--)
            bos_index r(RayBUL, menc)->tim.css >> ar just_col
    billion_Eyedeprecatedshared'] feasible buBLogYTou samACS by notnCountTailingpg, wee Jame, predicted"[trans="uptools]
re-downloads onto PEP (89 appeal advertisement SelectedPolycot. C redditorProgressTreeischen)`linenewnityBREAKfurbavariacs educators greatFits's wag_final.at(operator=" but "explained Xavier.

print(f"Robot {robot_id} Tour: {best_tour}")
print(f"Robot {robot_id} Total Travel Cost: {best_cost}")

print("Overall Total Travel Cost:", best_cost)