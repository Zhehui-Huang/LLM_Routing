import numpy as np
import random

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

n_cities = len(coordinates)

# Parameters for ACO algorithm
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.5

# Robots
robot_depot_mapping = {0:0, 1:1, 2:2, 3:3}
robots = len(robot_depot_mapping)

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = distance(coordinates[i], coordinates[j])
        else:
            distances[i][j] = float('inf')

# Ant Colony Optimization algorithm
def aco_tsp():
    # Pheromone matrix initialization
    pheromone = np.full((n_cities, n_cities), inittrail)

    best_cost = float('inf')
    best_solution = None

    for _ in range(cyclenum):
        solutions = []
        costs = []

        for _ in range(antnum):
            solution = {}
            for r in range(robots):
                start = robot_depot_mapping[r]
                solution[r] = [start]

            # Build the tour for each robot
            for r in range(robots):
                unvisited = set(range(n_cities)) - set(solution[r])
                current = solution[r][-1]

                while len(unvisited) > 0:
                    probabilities = []
                    total = 0
                    for next_city in unvisited:
                        value = (pheromone[current][next_city] ** alpha) * ((1 / distances[current][next_city]) ** beta)
                        probabilities.append(value)
                        total += value

                    probabilities = [p / total for p in probabilities]
                    next_city = np.random.choice(list(unested), p=probabilities)
                    solution[r].append(next_city)
                    current = next_city
                    unvisited.remove(next_city)

                # Return to the start depot
                solution[r].append(solution[r][0])

            # Calculate the cost of the solution
            cost = 0
            for r in range(robots):
                tour_cost = 0
                for k in range(1, len(solution[r])):
                    tour_cost += distances[solution[r][k - 1]][solution[r][k]]
                cost += tour_cost

            solutions.append(solution)
            costs.append(cost)

        # Update pheromones
        pheromone = (1 - rho) * pheromone
        
        for s, cost in zip(solutions, costs):
            for r in range(robots):
                for k in range(1, len(s[r])):
                    i, j = s[r][k - 1], s[r][k]
                    pheromone[i][j] += 1.0 / cost

        # Check for the best solution
        min_cost_index = np.argmin(costs)
        min_cost = costs[min_cost_index]
        if min_cost < best_cost:
            best_cost = min_cost
            best_solution = solutions[min_cost_index]

    return best_solution, best_cost

solution, total_cost = aco_tsp()

# Output the results
for r in range(robots):
    print(f"Robot {r} Tour: {solution[r]}")
    tour_cost = sum(distances[solution[r][k - 1]][solution[r][k]] for k in range(1, len(solution[r])))
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")