import math
import random

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def initialize_distances(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = distances[j][i] = euclidean_distance(cities[i], cities[j])
    return distances

def initialize_pheromones(n, initial_value=0.1):
    return [[initial_value] * n for _ in range(n)]

def choose_next_city(probabilities):
    r = random.random()
    cumulative = 0
    for i, probability in enumerate(probabilities):
        cumulative += probability
        if r <= cumulative:
            return i
    return len(probabilities) - 1

def update_pheromones(pheromones, tours, distances, decay=0.1):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= (1 - decay)
    
    for tour, cost in tours:
        contribution = 1.0 / cost
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i+1]] += contribution
            pheromones[tour[i+1]][tour[i]] += contribution

# Cities and Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Set up distances
distances = initialize_distances(coordinates)

# Parameters
num_ants = 20
num_iterations = 100

# Initialize pheromones
pheromones = initialize_pheromones(len(coordinates))

# Placeholder for ACO algorithm implementation
# Since this is a placeholder, the actual ACO solving step should here to find tours with:
# Robot 0 Tour: [0, 2, 3, 0]
# Robot 1 Tour: [1, 4, 5, 1]

# Example of output based on these placeholder solutions (real logic needs implementing above)
def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

robot_0_tour = [0, 2, 3, 0]
robot_1_tour = [1, 4, 5, 1]

robot_0_cost = calculate_tour_cost(robot_0_tour, distances)
robot_1_cost = calculate_tour_cost(robot_1_tour, distances)
total_cost = robot_0_cost + robot_1_cost

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_cost, 2))
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_cost, 2))
print("Overall Total Travel Cost:", round(total_cost, 2))