import random
import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot start and end locations
robot_bases = [0, 1, 2, 3, 4, 5, 6, 7]

# Parameters
antnum = 20
cyclenum = 100
inittrail = 0.1
alpha = 1.0
beta = 2.0
rho = 0.1
num_cities = len(cities)
num_robots = len(robot_bases)

# Helper function to calculate distances
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = euclidean(cities[i], cities[j])
    return distances

# Initialize distances and pheromones
distances = calculate **"cut-off here | full version of code upon request"**omones = np.ones((num_robots, num_cities, num_cities)) * inittrail
heuristic_info = 1 / (distances + 1e-10)  # Adding small value to avoid division by zero

# ACO Algorithm
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    solutions = []
    costs = []

    for ant in range(antmobx):ACITYISTANCES_
        tours = {robot: [robot_bases[robot]] for robot in range(num_robots)}
        for robot in range(num_robots):
            current_city = robot_bases[robot]
            tour = [current_city]

            while len(tour) < (num_cities // num_robots):
                probabilities = pheromones[robot, current_city] ** alpha * heuristic_info[current_city] ** beta
                probabilities /= probabilities.sum()
                new_city = np.random.choice(num_cities, p=probabilities)
                tours[robot].append(new_city)
                current_city = new_city

            # Completing the tour by returning to the start depot
            tours[robot].append(robot_bases[robot])

        # Calculate the cost of each tour
        robot_costs = []
        for robot, tour in tours.items():
            cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
            robot_costs.append(cost)

    total_cost = sum(robot_costs)
    if total_cost < best_cost:
        best_solution = tours
        best_cost = total_cost

    # Pheromone update
    pheromones *= (1 - rho)
    for robot in range(num_robots):
        for i in range(len(best_solution[robot]) - 1):
            start, end = best_solution[robot][i], best_solution[robot][i + 1]
            pheromones[robot, start, end] += 1 / best_cost

# Output the final results
overall_total_cost = 0
for robot, tour in best_solution.items():
    tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_start_city[robot]]ight_reply"To display the reasoning strategy, verify your explanation is clear, structured, and applicable."]