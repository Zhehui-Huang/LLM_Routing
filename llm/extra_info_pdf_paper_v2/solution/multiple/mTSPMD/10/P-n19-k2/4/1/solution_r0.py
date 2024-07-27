import numpy as np
import random

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distance_matrix[i][j] = euclidean_window_distance(cities[i], cities[j])

# Ant Colony Parameters
num_ants = 20
pheromone = np.ones_like(distance_matrix)
desirability = 1 / (distance_matrix + 1e-10)  # To avoid division by zero
evaporation_rate = 0.5
pheromone_deposit = 1.0

def choose_next_city(current_city, visited):
    probabilities = pheromone[current_city] * desirability[current_city] ** 2
    probabilities[visited] = 0
    if probabilities.sum() == 0:  # Avoid division by zero if everything's visited
        return -1
    probabilities /= probabilities.sum()
    next_city = np.random.choice(len(cities), p=probabilities)
    return next_city

def update_pheromone(tours, costs):
    global pheromone
    pheromone *= (1 - evaporation_rate)
    for tour, cost in zip(tours, costs):
        additional_pheromone = pheromone_deposit / cost
        for i in range(len(tour)-1):
            pheromone[tour[i]][tour[i+1]] += additional_pheromone
            pheromone[tour[i+1]][tour[i]] += additional_pheromone  # Because it's a symmetric TSP

# Simulation loop
def simulate():
    best_tours = []
    best_costs = []
    best_total_cost = float('inf')

    for _ in range(100):  # Number of iterations
        tours = []
        costs = []

        for depot in [0, 1]:
            for _ in range(num_ants // 2):
                tour = [depot]
                visited = set(tour)
                cost = 0
                while len(visited) < len(cities):
                    current = tour[-1]
                    next_city = choose_next_city(current, visited)
                    if next_city == -1:
                        break
                    tour.append(next_city)
                    cost += distance_matrix[current][next_city]
                    visited.add(next_city)

                tour.append(depot)
                cost += distance_matrix[tour[-2]][depot]
                tours.append(tour)
                costs.append(cost)

        if sum(costs) < best_total_cost:
            best_total_cost = sum(costs)
            best_tours = tours
            best_costs = costs

        update_pheromone(tours, costs)

    return best_tours, best_costs, best_total_cost

best_tours, best_costs, best_total_cost = simulate()

for i, (tour, cost) in enumerate(zip(best_tours, best_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")