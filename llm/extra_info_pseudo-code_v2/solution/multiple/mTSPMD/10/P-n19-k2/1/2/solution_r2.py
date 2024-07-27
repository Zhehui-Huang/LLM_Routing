import numpy as as np
import random

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52),
    (49, 43), (52, 64),
    (31, 62), (52, 33),
    (42, 41), (52, 41),
    (57, 58), (62, 42),
    (42, 57), (27, 68),
    (43, 67), (58, 27),
    (37, 69), (61, 33),
    (62, 63), (63, 69),
    (45, 35)
]

num_cities = len(coordinates)
depots = [0, 1]

# Parameters for the ACO
ant_count = 20
max_no_improvement = 50
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
initial_pheromone = 1.0

# Pheromone matrix initialization
pheromones = np.full((num_cities, num_cities), initial_pheromone)

def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.hypot(x2 - x1, y2 - y1)

# Distance matrix computation
distances = np.array([[distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

def calculate_total_cost(tours):
    return sum(distances[tour[i], tour[i + 1]] for tour in tours for i in range(len(tour) - 1))

def aco_solve():
    global pheromones
    best_tours = None
    best_cost = float('inf')
    no_improvement_runs = 0

    while no_improvement_runs < max_no_improvement:
        colony_tours = []
        
        for _ in range(ant_count):
            starting_depot = random.choice(depots)  # Start at a random depot
            tour = [starting_depot]
            visited = set(tour)

            while len(visited) < num_cities:
                current = tour[-1]
                probabilities = []

                # Calculate probabilities to move to the next city
                for next_city in range(num_cities):
                    if next_city not in visited:
                        trail = pheromones[current][next_city] ** alpha
                        visibility = (1.0 / distances[current][next_city]) ** beta
                        probabilities.append(trail * visibility)
                    else:
                        probabilities.append(0)

                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()

                # Choose the next city
                next_city = np.random.choice(range(num_cities), p=probabilities)
                tour.append(next_city)
                visited.add(next_city)

            tour.append(starting_depot)  # Return to the depot
            colony_tours.append(tour)

        # Pheromone evaporation
        pheromones *= (1 - evaporation_rate)

        # Pheromone update
        for tour in colony_tours:
            cost = calculate_total_cost([tour])
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += 1 / cost

        # Check for the best solution
        for tour in colony_tours:
            cost = calculate_total_cost([tour])
            if cost < best_cost:
                best_cost = cost
                best_tours = tour
                no_improvement_runs = 0
            else:
                no_improvement_runs += 1

    return best_tours, best_cost

# Compute the tours and total travel cost
best_tours, total_cost = aco_solve()
robot_tours = [best_tours[:], best_tours[:]]  # Assuming we separate the tour half-half for simplicity

for idx, robot_tour in enumerate(robot_tours):
    robot_cost = calculate_total_cost([robot_tour])
    print(f"Robot {idx} Tour: {robot_tour}")
    print(f"Robot {idx} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")