import numpy as np
from math import sqrt

# City coordinates
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
          7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
          13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 
          19: (63, 69), 20: (45, 35)}

# Distance matrix computation
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

dist_matrix = [[distance(cities[i], cities[j]) for j in cities] for i in cities]

# Minimalistic ACO Parameters
ant_count = 5
generations = 50
alpha = 1.0
beta = 2.0
rho = 0.5
initial_pheromone = 1.0 / len(cities)

pheromones = [[initial_pheromone] * len(cities) for _ in range(len(cities))]

def choose_next_city(current_city, visited):
    probabilities = []
    pheromone = [pheromones[current_city][i] ** alpha for i in range(len(cities))]
    heuristic = [1.0 / (dist_matrix[current_city][i] ** beta) if i not in visited else 0 for i in range(len(cities))]
    probabilities = [pheromone[i] * heuristic[i] for i in range(len(cities))]

    if sum(probabilities) == 0:
        probabilities = [0 if i in visited else 1 for i in range(len(cities))]

    probabilities /= np.sum(probabilities)
    return np.random.choice(range(len(cities)), p=probabilities)

def update_pheromones(tours, costs):
    for i, tour in enumerate(tours):
        for j in range(1, len(tour)):
            pheromones[tour[j-1]][tour[j]] += 1.0 / costs[i]

def ant_colony_optimization():
    best_tours = []
    best_costs = [float('inf'), float('inf')]

    for generation in range(generations):
        tours = [[0], [1]]
        costs = [0, 0]

        for k in range(2):
            visited = set(tours[k])
            while len(visited) < len(cities):
                current_city = tours[k][-1]
                next_city = choose_next_city(current_city, visited)
                tours[k].append(next_city)
                visited.add(next_city)
                costs[k] += dist_matrix[current_city][next_city]
                if len(visited) == len(cities): break
            tours[k].append(tours[k][0])
            costs[k] += dist_matrix[tours[k][-2]][tours[k][-1]]

        for i in range(2):
            if costs[i] < best_costs[i]:
                best_costs[i] = costs[i]
                best_tours[i] = tours[i]

        update_pheromones(tours, costs)
        pheromones = [[(1 - rho) * pheromone + initial_pheromone for pheromone in row] for row in pheromones]

    return best_tours, best_costs

best_tours, best_costs = ant_colony_optimization()

# Output adjustment
total_cost = sum(best_costs)
print(f"Robot 0 Tour: {best_tours[0]}")
print(f"Robot 0 Total Travel Cost: {best_costs[0]}")
print(f"Robot 1 Tour: {best_tours[1]}")
print(f"Robot 1 Total Travel Cost: {best_costs[1]}")
print(f"Overall Total Travel Cost: {total_cost}")