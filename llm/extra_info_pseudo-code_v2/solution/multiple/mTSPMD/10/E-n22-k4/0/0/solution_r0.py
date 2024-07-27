import math
import random

# Define cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Constants
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.5
num_cities = len(cities)
num_robots = 4
depots = [0, 1, 2, 3]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initialize the pheromone levels
pheromone = [[inittrail for _ in range(num_cities)] for _ in range(num_cities)]

# Heuristic information matrix (inverse of distances)
eta = [[1.0/distance(i, j) if i != j else 0 for j in range(num_cities)] for i in range(num_cities)]

# Function to perform ant colony optimization
def ant_colony_optimization():
    best_tours = None
    best_cost = float('inf')
    stagnation = 0
    solutions = []

    for cycle in range(cyclenum):
        tours = []
        costs = []

        for ant in range(antnum):
            tour = [random.choice(depots)]
            while len(tour) < num_cities + 1:
                current = tour[-1]
                probabilities = [(pheromone[current][j] ** alpha) * (eta[current][j] ** beta) if j not in tour else 0 for j in range(num_cities)]
                if sum(probabilities) == 0:
                    break  # Trapped, should not happen ideally
                probabilities = [p / sum(probabilities) for p in probabilities]
                next_city = random.choices(range(num_cities), weights=probabilities)[0]
                tour.append(next_city)
            
            tour.append(tour[0])  # Return to depot
            tours.append(tour)
            cost = sum(distance(tour[k], tour[k+1]) for k in range(len(tour) - 1))
            costs.append(cost)

        # Store best result
        index_min = min(range(len(costs)), key=costs.__getitem__)
        if costs[index_min] < best_cost:
            best_cost = costs[index_min]
            best_tours = tours[index_min]
            stagnation = 0
        else:
            stagnation += 1

        # Update pheromones
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone[i][j] *= (1 - rho)
        
        for t, cost in zip(tours, costs):
            for k in range(len(t)-1):
                i, j = t[k], t[k+1]
                pheromone[i][j] += 1.0 / cost

        # Break if stagnation criteria met
        if stagnation >= 10:
            break

    return best_tours, best_cost

# Running the optimization
best_tours, overall_total_cost = ant_colony_optimization()

# Print results
robot_tours = {i: [] for i in range(num_robots)}
for i in range(num_robots):
    robot_tours[i] = [depots[i]] + [city for city in best_tours if city not in depots and city not in robot_tours[i]] + [depots[i]]
    tour_cost = sum(distance(robot_tours[i][j], robot_tours[i][j+1]) for j in range(len(robot_tours[i])-1))
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")