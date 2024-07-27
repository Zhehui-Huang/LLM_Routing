import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates (index 0-7 are depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and their respective start-end depots
robots = {i: i for i in range(8)}

# Distance matrix calculation
def calculate_distance_matrix(coords):
    size = len(coords)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Ant colony optimization parameters
n_ants = 30
n_iterations = 100
decay = 0.1
alpha = 1  # Importance of pheromone
beta = 5   # Importance of heuristic information (inverse of distance)
Q = 10     # Pheromone left per unit of travel

distance_matrix = calculate_distance_matrix(coordinates)

# Pheromone matrix
pheromone = np.ones_like(distance_matrix) * 0.1

# Heuristic information matrix - inverse of the distance matrix
heuristic = 1 / (distance_matrix + 1)  # To avoid division by zero error

def aco_tour_for_robot(depot):
    best_cost = float('inf')
    best_tour = None
    for _ in range(n_iterations):
        # Ant tours start and end at the assigned depot
        tours = [[depot] for _ in range(n_ants)]
        costs = [0 for _ in range(n_ants)]
        for _ in range(len(coordinates) - 1):  # Each ant makes n - 1 moves
            for ant in range(n_ants):
                current_city = tours[ant][-1]
                probabilities = pheromone[current_city] ** alpha * heuristic[current_city] ** beta
                probabilities[tours[ant]] = 0  # Cannot visit alread visited cities
                probabilities /= probabilities.sum()
                next_city = np.random.choice(range(len(coordinates)), p=probabilities)
                tours[ant].append(next_city)
                costs[ant] += distance_matrix[current_city][next_city]
        # Return to the starting depot
        for ant in range(n_ants):
            costs[ant] += distance_matrix[tours[ant][-1]][depot]
            tours[ant].append(depot)
            if costs[ant] < best_cost:
                best_cost = costs[ant]
                best_tour = tours[ant]
        
        # Pheromone update
        pheromone *= (1 - decay)
        for ant in range(n_ants):
            for i in range(len(tours[ant]) - 1):
                pheromone[tours[ant][i]][tours[ant][i + 1]] += Q / costs[ant]

    return best_tour, best_cost

all_tours = []
total_cost = 0

for robot, depot in robots.items():
    tour, cost = aco_tour_for_robot(depot)
    all_tours.append((robot, tour, cost))
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")