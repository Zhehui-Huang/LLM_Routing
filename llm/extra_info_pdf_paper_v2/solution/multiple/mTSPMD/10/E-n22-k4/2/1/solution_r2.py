import numpy as np
from scipy.spatial.distance import euclidean

# City Coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Parameters
alpha = 1
beta = 5
pheromone_evaporation_rate = 0.1
pheromone_intensification = 10
iterations = 100
n_ants = 10

# Pheromone matrix initialization
pheromone = np.ones((n_cities, n_cities)) * 0.1

def choose_next_city(current_city, allowed_cities):
    probabilities = []
    for next_city in allowed_cities:
        if distance_matrix[current_city][next_city] != float('inf'):
            trail_strength = pheromone[current_city][next_city] ** alpha
            visibility = 1 / distance_matrix[current_city][next_city] ** beta
            probabilities.append(trail_strength * visibility)
        else:
            probabilities.append(0)
    
    probabilities = probabilities / np.sum(probabilities)
    return np.random.choice(allowed_cities, p=probabilities)
    
def update_pheromone(pheromone, tours, costs):
    for k in range(len(tours)):
        for i in range(len(tours[k]) - 1):
            from_city = tours[k][i]
            to_city = tours[k][i + 1]
            pheromone[from_city][to_city] += pheromone_intensification / costs[k]
    pheromone *= (1 - pheromone_evaporation_rate)
    return pheromone

# Robot configurations
robots = {
    0: [0] + list(range(4, 12)),
    1: [1] + list(range(12, 16)),
    2: [2] + list(range(16, 18)),
    3: [3] + list(range(18, 22))
}

# Perform tours for each robot
all_tours = []
total_cost = 0
for robot_id, assigned_cities in robots.items():
    best_cost = float('inf')
    best_tour = None

    for _ in range(iterations):
        tours = []
        costs = []
        for __ in range(n_ants):
            tour = [assigned_cities[0]]
            remaining_cities = assigned_cities[1:]
            while remaining_cities:
                next_city = choose_next_city(tour[-1], remaining_cities)
                tour.append(next_city)
                remaining_cities.remove(next_city)
            tour.append(assigned_cities[0])  # complete the tour by returning to the depot
            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            tours.append(tour)
            costs.append(tour_cost)

        # Update pheromones
        pheromone = update_pheromone(pheromone, tours, costs)

        # Identify the best tour in current iteration
        for cost, tour in zip(costs, tours):
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

    all_tours.append((robot_id, best_tour))
    total_cost += best_cost

# Output results
for robot_id, tour in all_tours:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))}")

print(f"Overall Total Travel Cost: {total_cost}")