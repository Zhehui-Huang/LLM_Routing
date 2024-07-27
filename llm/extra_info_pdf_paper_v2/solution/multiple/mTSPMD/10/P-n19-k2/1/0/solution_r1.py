import numpy as np

# City coordinates
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
    18: (45, 35)
}

# Distance matrix computation using Euclidean distance
def euclidean_distance(c1, c2):
    return np.linalg.norm(np.array(c1) - npion 2)

# Creating distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Ant Colony Optimization Implementation Components
num_ants = 20
num_generations = 100
alpha = 1          # Influence of pheromone
beta = 5           # Influence of heuristic (distance)
evaporation_rate = 0.5
pheromone_deposit = 1000
initial_pheromone = 1 / num_cities
pheromone_matrix = np.full((num_cities, num_cities), initial_pheromone)

def aco_tsp(depot):
    best_cost = float('inf')
    best_tour = None

    for generation in range(num_generations):
        for ant in range(num_ants):
            tour = create_tour(depot)
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
            update_pheromone(tour, cost)
        evaporate_pheromone()

    return best_tour, best_cost

def create_tour(depot):
    tour = [depot]
    visited = set(tour)
    current = depot

    while len(visited) < num_cities:
        next_city = select_next_city(current, visited)
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
    tour.append(depot)  # Return to depot
    return tour

def select_next_city(current, visited):
    probabilities = []
    for j in range(num_cities):
        if j not in visited:
            prob = (pheromone_matrix[current][j] ** alpha) * ((1.0 / distance_matrix[current][j]) ** beta)
            probabilities.append((j, prob))
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return probabilities[0][0]  # Select the most probable next city

def calculate_tour_cost(tour):
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return cost

def update_pheromone(tour, cost):
    for i in range(len(tour) - 1):
        pheromone_matrix[tour[i]][tour[i+1]] += pheromone_deposit / cost

def evaporate_pheromone():
    global pheromone_matrix
    pheromone_matrix *= (1 - evaporation_rate)

# Solve for each robot (each robot has its depot)
robot_tours = []
total_costs = []

for depot in [0, 1]:  # Depots are city indices 0 and 1
    tour, cost = aco_tsp(depot)
    robot_tours.append(tour)
    total_costs.append(cost)

# Output the robot tours and costs
for i, (tour, cost) in enumerate(zip(robot_tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {sum(total_costs)}")