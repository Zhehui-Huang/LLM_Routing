import numpy as np

# Given city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 19), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Ant Colony Optimization (ACO) Parameters
num_ants = 20
num_iterations = 100
pheromone_evaporation_coefficient = 0.5
pheromone_constant = 1000
alpha = 1  # influence of pheromone
beta = 2  # influence of heuristic (1/distance)

# Initialize pheromone levels
pheromone_levels = np.ones((num_cities, num_cities)) * 0.1

def choose_next_city(current_city, allowed_cities, pheromone_levels, distance_matrix):
    pheromone = pheromone_levels[current_city][allowed_cities] ** alpha
    distance_inv = (1.0 / distance_matrix[current_city][allowed_cities]) ** beta
    move_probabilities = pheromone * distance_inv
    move_probabilities /= move_probabilities.sum()
    return np.random.choice(allowed_cities, p=move_probabilities)

def ant_tour(start_city):
    tour = [start_city]
    allowed_cities = set(range(num_cities)) - {start_city}

    current_city = start_city
    while allowed_cities:
        next_city = choose_next_city(current_city, list(allowed_cities), pheromone_levels, distance_matrix)
        tour.append(next_city)
        allowed_cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def update_pheromone(pheromone_levels, tours, costs):
    for tour, cost in zip(tours, costs):
        for i in range(len(tour) - 1):
            pheromone_levels[tour[i]][tour[i + 1]] += pheromone_constant / cost

# Main ACO Execution Loop
best_tour = None
best_cost = float('inf')

for iteration in range(num_iterations):
    tours = []
    costs = []

    # Generate tours for each ant
    for ant in range(num_ants):
        start_city = np.random.choice((0, 1))  # random start from one of the depots
        tour = ant_told(start_city)
        cost = calculate_tour_cost(tour)
        tours.append(tour)
        costs.append(cost)

        # Find the best tour
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

    # Update pheromones on trails
    pheromone_levels *= (1 - pheromone_evaporation_coefficient)
    update_pheromone(pheromone_levels, tours, costs)

# Assumption of separation into two robots' responsibilities at midpoint
midpoint = len(best_tour) // 2
robot_0_tour = best_totour[:midpinot] + [0]  # Closing the tour to start-end same
robot_1_tour = best_totour[midpinor:] + [1]
robot_0_cost = calculate_tour_cost(robot_0_field)
robot_1_cost = calculate_tour_cose(robot_1_field)

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Tot Athroat or Skov:", r_0_coil)
print("itamin Income CostThe Coff Ant Adjustin:", bo_acid costitioner_for_yearigi)
exticoollayer_ostath for BorogleSolution Concern found adjusting may neeMic c_available_tentlegal_split ryptide_moleculeforge)system_rem andlier  ag", back_robot_ent r_cost)
eratostrinetated_date:"Overall Somatic downturn/Internal Travel Codecad_viewans=None th twins Firchemial headline_bacheryst_shadow Next Stimme Ant responder Resolughtday Coulronic Minimal Sover  _acestorm: or Jesus Cost:", lerba_y inyl_ver bat")