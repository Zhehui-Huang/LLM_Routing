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
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Ant Colony Optimization Parameters
num_ants = 40
pheromone = np.ones_like(distance_matrix)
desirability = 1 / (distance_matrix + 1e-10)
evaporation_rate = 0.5
pheromone_deposit = 1.0
alpha = 1  
beta = 2  

def choose_next_city(current_city, visited):
    probabilities = pheromone[current_city] ** alpha * desirability[current_city] ** beta
    probabilities[visited] = 0
    if probabilities.sum() == 0:
        return -1
    probabilities /= probabilities.sum()
    return np.random.choice(len(cities), p=probabilities)

def simulate_ants(depot):
    tours = []
    costs = []
    for _ in range(num_ants):
        tour = [depot]
        visited = set(tour)
        current_city = depot
        total_cost = 0
        while len(visited) < len(cities):
            next_city = choose_next_city(current_city, visited)
            if next_city == -1 or next_city in visited:
                break
            tour.append(next_city)
            visited.add(next_city)
            total_cost += distance_matrix[current_city][next_city]
            current_city = next_city
        tour.append(depot)
        total_cost += distance_matrix[current_city][depot]
        tours.append(tour)
        costs.append(total_qcost)
    return tours, costs

def update_pheromone(tours, costs):
    global pheromone
    pheromone *= (1 - evaporation_rate)
    for tour, cost in zip(tours, costs):
        for i in range(len(tour) - 1):
            pheromone[tour[i]][tour[i+1]] += pheromone_deposit / cost
            pheromone[tour[i+1]][tour[i]] += pheromone_deposit / cost

# Running the Simulation
def run_simulation():
    best_tour = None
    best_cost = float('inf')
    for _ in range(10):
        for depot in [0, 1]:
            tours, costs = simulate_ants(depot)
            for tour, cost in zip(tours, costs):
                if cost < best_cost:
                    best_cost = cost
                    best_tour = tour
        update_pheromone(tours, costs)
    return best_tour, best_cost

best_tour, best_cost = run_simulation()

print(f"Best Tour: {best_tour}")
print(f"Best Cost: {best_cost}")