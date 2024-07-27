import numpy as np

# Constants and initial setup
NUM_CITIES = 19
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

def euclidean_distance(a, b):
    return np.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Initialize pheromone trails
pheromones = np.ones((NUM_CITIES, NUM_CITIES))
desirability = np.zeros((NUM_CITIES, NUM_CITIES))

for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        if i != j:
            desirability[i][j] = 1 / euclidean_distance(i, j)

# Hyperparameters for the algorithm
alpha = 1.0
beta = 5.0
rho = 0.1
ant_count = 20
iterations = 100

def select_next_city(current_city, visited):
    probs = np.zeros(NUM_CITIES)
    for city in range(NUM_CITIES):
        if city not in visited:
            probs[city] = pheromones[current_city][city]**alpha * desirability[current_city][city]**beta
    if probs.sum() == 0:
        return random.choice([city for city in range(NUM_CITIES) if city not in visited])
    probs /= probs.sum()
    return np.random.choice(NUM_CITIES, p=probs)

def simulate_ant(depots):
    tours = []
    costs = []
    for depot in depots:
        tour = [depot]
        total_cost = 0
        visited = set(tour)
        current_city = depot
        while len(visited) < NUM_CITIES:
            next_city = select_next_city(current_city, visited)
            tour.append(next_city)
            total_cost += euclidean_distance(current_city, next_city)
            current_city = next_city
            visited.add(next_city)
        tour.append(depot) # return to depot
        total_cost += euclidean_distance(current_city, depot)
        tours.append(tour)
        costs.append(total_cost)
    return tours, costs

# Run simulation for a specified number of iterations
depots = [0, 1]
all_tours, all_costs = [], []
for _ in range(iterations):
    tours, costs = simulate_ant(depots)
    all_tours.append(tours)
    all_costs.append(costs)

# Get the best solution
min_cost_idx = np.argmin([sum(cost) for cost in all_costs])
best_tours = all_tours[min_cost_idx]
best_costs = all_costs[min_cost_idx]
overall_cost = sum(best_costs)

# Output results
for idx, (tour, cost) in enumerate(zip(best_tours, best_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")