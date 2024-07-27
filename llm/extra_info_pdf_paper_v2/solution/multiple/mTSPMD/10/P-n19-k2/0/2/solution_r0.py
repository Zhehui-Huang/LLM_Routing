import numpy as np

# Constants
num_cities = 19
num_robots = 2
depot_cities = [0, 1]
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
               (62, 63), (63, 69), (45, 35)]

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return np.linalg.norm(np.array(coordinates[city1]) - np.array(coordinates[city2]))

# Initialize distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calc_distance(i, j)

# ACO parameters
num_ants = 40
max_iterations = 100
alpha = 1.0  # pheromone importance
beta = 2.0  # distance importance
evaporation_rate = 0.5
pheromone_deposit = 0.1
initial_pheromone = 0.1

# Pheromone matrix
pheromone_matrix = np.full((num_cities, num_cities), initial_pheromone)

def aco_algorithm():
    best_tour_length = float('inf')
    best_solutions = []

    for iteration in range(max_iterations):
        all_tours = []
        all_cost = []

        for ant in range(num_ants):
            # Select starting points for robots
            tours = {r: [depot_cities[r]] for r in range(num_robots)}
            unvisited = set(range(num_cities)) - set(depot_cities)

            for robot in range(num_robots):
                current = depot_cities[robot]
                while unvisited:
                    probabilities = []
                    for next_city in unfiltered_cities:
                        if next_city in unvisited or next_city == depot_cities[robot]:
                            pheromone_level = pheromone_matrix[current][next_city]**alpha
                            heuristic_value = (1 / distance_matrix[current][next_city])**beta
                            probabilities.append((next_city, pheromone_level * heuristic_value))
                    
                    next_city = max(probabilities, key=lambda x: x[1])[0] if probabilities else depot_cities[robot]

                    if next_city == depot_cities[robot]:
                        break

                    tours[robot].append(next_city)
                    unvisited.remove(next_city)
                    current = next_city

                tours[robot].append(depot_cities[robot])

            all_tours.append(tours)

            # Calculate cost
            total_cost = 0
            for robot, tour in tours.items():
                tour_cost = 0
                for i in range(len(tour) - 1):
                    tour_cost += distance_matrix[tour[i]][tour[i + 1]]
                total_cost += tour_cost
                all_cost.append((tour_cost, tours))
        
        # Find best tour based on cost
        best_tour = min(all_cost)
        if best_tour[0] < best_tour_length:
            best_tour_length = best_tour[0]
            best_solutions = best_tour[1]

        # Update pheromones
        pheromone_matrix *= (1 - evaporation_rate)
        for robot, tour in best_solutions.items():
            for i in range(len(tour) - 1):
                pheromone_matrix[tour[i]][tour[i + 1]] += pheromone_deposit

    return best_solutions, best_tour_length

best_solution, overall_cost = aco_algorithm()

for robot, tour in best_solution.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))}")

print(f"Overall Total Travel Cost: {overall_cost}")