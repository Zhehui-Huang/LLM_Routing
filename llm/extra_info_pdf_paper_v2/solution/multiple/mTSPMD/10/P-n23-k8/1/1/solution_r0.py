import numpy as np
import random
import math

# Define the coordinates of each depot and city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Distances between all pairs of cities using Euclidean distance
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = math.dist(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Number of depots and robots
number_of_depots = 8
robots = [i for i in range(number_of_depots)]
depots = [i for i in range(number_of_depots)]

# Algorithm settings
num_ants = 20
num_iterations = 100
alpha = 1.0
beta = 5.0
rho = 0.1
initial_pheromone = 1 / (len(coordinates) * random.choice(list(np.diag(distance_matrix))))

# Pheromone matrix
pheromones = np.full((len(coordinates), len(coordinates)), initial_pheromone)

def closest_depot(city, depots):
    return min(depots, key=lambda depot: distance_matrix[city][depot])

def roulette_wheel(probabilities):
    cumulative_prob = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    r = random.random()
    for i, prob in enumerate(cumulative_prob):
        if r <= prob:
            return i
    return len(probabilities) - 1

def update_pheromone(pheromones, tours, costs):
    for i, cost in enumerate(costs):
        for j in range(len(tours[i]) - 1):
            pheromones[tours[i][j]][tours[i][j + 1]] += 1 / cost
    pheromones *= (1 - rho)

def ant_colony_optimization():
    best_solution = None
    best_cost = float('inf')
    for _ in range(num_iterations):
        solutions = []
        tours = []
        costs = []
        for ant in range(num_ants):
            tour = []
            cost = 0
            for robot in robots:
                # Each ant starts a construction cycle for a robot's tour
                current_city = depots[robot]
                tour = [current_city]
                unvisited = set(range(len(coordinates))) - set(depots)
                while unvisited:
                    probabilities = []
                    for city in unvisited:
                        tau = pheromones[current_city][city] ** alpha
                        eta = (1 / distance_matrix[current_city][city]) ** beta
                        probabilities.append(tau * eta)
                    probabilities = [p / sum(probabilities) for p in probabilities]
                    next_city = roulette_wheel(probabilities)
                    next_city = list(unvisited)[next_city]
                    tour.append(next_city)
                    cost += distance_matrix[current_city][next_city]
                    current_city = next_city
                    unvisited.remove(next_city)
                tour.append(depots[robot])
                cost += distance_matrix[current_city][depots[robot]]
                solutions.append(tour)
                costs.append(cost)
            if sum(costs) < best_cost:
                best_cost = sum(costs)
        update_pheromone(pheromones, solutions, costs)
    return best_solution, best_cost

best_solution, best_cost = ant_colony_optimization()

# Output the solution according to requirements
print(f"Overall Total Travel Cost: {best_cost}")
for i, robot_tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {calculate_tour_cost(robot_tour, distance_matrix)}")