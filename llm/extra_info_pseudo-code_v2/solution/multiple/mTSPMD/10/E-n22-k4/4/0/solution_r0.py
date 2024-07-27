import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Parameters
num_cities = len(coordinates)
num_robots = 4
depots = [0, 1, 2, 3]
alpha = 1.0
beta = 5.0
rho = 0.1
antnum = 10
cyclenum = 100
init_pheromone = 1.0

# Distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Heuristic information matrix (inverse of the distance)
eta = 1 / (distance_matrix + 1e-10)

# Pheromone matrix
pheromones = np.full((num_cities, num_cities), init_pheromone)

def calculate_transition_probabilities(city, allowed):
    denom = sum((pheromones[city, j]**alpha) * (eta[city, j]**beta) for j in allowed)
    probs = [(pheromones[city, j]**alpha) * (eta[city, j]**beta) / denom if j in allowed else 0 for j in range(num_cities)]
    return probs

def ant_tour(start_city):
    tour = [start_city]
    current_city = start_city
    allowed = list(set(range(num_cities)) - set(depots) - {current_city})

    while allowed:
        transition_probs = calculate_transition_probabilities(current_city, allowed)
        next_city = np.random.choice(num_cities, p=transition_probs)
        tour.append(next_city)
        current_city = next_city
        allowed.remove(next_city)

    tour.append(start_city)  # Return to depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def update_pheromones(all_tours):
    for tour in all_tours:
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            pheromones[from_city, to_city] += 1 / calculate_tour_cost(tour)

best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    all_tours = []
    for robot_id in range(num_robots):
        tour = ant_tour(depots[robot_id])
        all_tours.append(tour)
    
    # Update pheromones
    pheromones *= (1 - rho)  # Evaporation
    update_pheromones(all_tours)

    # Check for best solution
    total_cost = sum(calculate_tour_cost(tour) for tour in all_tours)
    if total_cost < best_cost:
        best_cost = total_cost
        best_solution = all_tours

# Output solutions
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = calculate_tour_cost(tour)
    overall_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")