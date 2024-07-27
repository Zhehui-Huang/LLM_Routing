import numpy as np
import random

# Coordinates for each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots is equal to number of depots
depots = list(range(8))  # Robots 0-7 start at depots 0-7 respectively

# Compute distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Algorithm parameters
antnum = 20
cyclenum = 1000
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
initial_pheromone = 1.0

# Pheromone matrix initialization
pheromone_matrix = np.full((len(cities), len(cities)), initial_pheromone)

def transition_probabilities(curr, allowed):
    probs = []
    for n in allowed:
        tau_ij = pheromone_matrix[curr][n] ** alpha
        eta_ij = (1 / distance_matrix[curr][n]) ** beta
        probs.append(tau_ij * eta_ij)
    total = sum(probs)
    probs = [p / total for p in probs]
    return probs

def solution_construction():
    tours = [[] for _ in depots]
    costs = np.zeros(len(depots))

    for robot_id in depots:
        tour = [robot_id]
        current_city = robot_id
        while len(tour) < (len(cities) // len(depots) + (len(tour) < len(cities) % len(depots))):
            allowed_cities = [c for c in cities.keys() if c not in tour]
            if not allowed_cities:
                break
            probs = transition_probabilities(current_city, allowed_cities)
            next_city = np.random.choice(allowed_cities, p=probs)
            tour.append(next_city)
            costs[robot_id] += distance_matrix[current_city][next_city]
            current_city = next_city
        tour.append(robot_id)
        costs[robotid] += distance_matrix[current_city, robot_id]
        tours[robot_id] = tour

    return tours, costs

for cycle in range(cyclenum):
    tours, costs = solution_construction()
    # Update pheromones
    pheromone_matrix *= (1 - evaporation_rate)
    for robot_id, tour in enumerate(tours):
        for i in range(len(tour) - 1):
            pheromone_matrix[tour[i]][tour[i+1]] += 1 / costs[robot_id]

# Final output
total_cost = np.sum(costs)
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_cost}")