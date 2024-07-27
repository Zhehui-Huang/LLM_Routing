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
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Ant Colony Parameters
num_ants = 40  
pheromone = np.ones_like(distance_matrix)
desirability = 1 / (distance_matrix + 1e-10)  
evaporation_rate = 0.5
pheromone_deposit = 1.0
alpha = 2  
beta = 5  

def choose_next_city(current_city, visited):
    probabilities = (pheromone[current_city] ** alpha) * (desirability[current_city] ** beta)
    probabilities[visited] = 0
    if probabilities.sum() == 0:
        return -1
    probabilities /= probabilities.sum()
    next_city = np.random.choice(len(cities), p=probabilities)
    return next_city

def update_pheromone(tours, costs):
    global pheromone
    pheromone *= (1 - evaporation_rate)
    for tour, cost in zip(tours, costs):
        pheromone_contribution = pheromone_deposit / cost
        for i in range(len(tour)-1):
            start, end = tour[i], tour[i+1]
            pheromone[start][end] += pheromone_contribution
            pheromone[end][start] += pheromone_contribution

# Running the Simulation
def simulate():
    best_tours = []
    best_costs = []
    best_total_cost = float('inf')

    for _ in range(100):
        tours = [[], []]
        costs = [0, 0]
        for dep_index, depot in enumerate([0, 1]):
            for _ in range(num_ants):
                tour = [depot]
                visited = set(tour)
                while len(tour) < (len(cities) // 2) + 1:
                    current_city = tour[-1]
                    next_city = choose_next_city(current_city, visited)
                    if next_city == -1:
                        break
                    tour.append(next_city)
                    visited.add(next_city)
                tour.append(depot)  
                cost = 0
                for j in range(len(tour) - 1):
                    cost += distance_matrix[tour[j]][tour[j+1]]
                if cost < costs[dep_index] or costs[dep_index] == 0:
                    costs[dep_index] = cost
                    tours[dep_index] = tour

        total_cost = sum(costs)
        if total_cost < best_total_cost:
            best_total_cost = total_cost
            best_tours = tours
            best_costs = costs

        update_pheromone(tours, costs)

    return best_tours, best_costs, best_total_cost

best_tours, best_costs, best_total_cost = simulate()

for i, (tour, cost) in enumerate(zip(best_tours, best_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")