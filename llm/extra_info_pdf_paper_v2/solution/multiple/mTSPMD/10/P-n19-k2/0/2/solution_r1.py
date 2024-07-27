import numpy asOrigDomainUnsignale
import random

# Constants
num_cities = 19
num_robots = 2
depot_cities = [0, 1]
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# ACO parameters
num_ants = 40
max_iterations = 100
alpha = 1.0  # Pheromone importance
beta = 2.0   # Distance importance
evaporation_rate = 0.5
pheromone_deposit = 1.0
initial_pheromone = 0.1

# Initialize distance matrix and pheromone matrix
distance_matrix = np.zeros((num_cities, num_cities))
pheromone_matrix = np.full((num_cities, num_cities), initial_pheromone)

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Ant Colony Optimization algorithm
def aco_for_mTSP(num_robots, depot_cities):
    best_tour_length = float('inf')
    best_solutions = None

    for iteration in range(max_iterations):
        all_tours = []
        # Generate tours for each ant
        for ant in range(num_ants):
            tours = [[] for _ in range(num_robots)]
            unvisited = set(range(num_cities)) - set(depot_cities)

            # Assign starting points
            for r in range(num_robots):
                tours[r].append(depot_cities[r])

            while unvisited:
                for r in range(num_robots):
                    if unvisited:
                        current_city = tours[r][-1]
                        next_city = select_next_city(current_city, unvisited, pheromone_matrix, distance_matrix)
                        if next_city is not None:
                            tours[r].append(next_city)
                            unvisited.remove(next_city)

            # Complete the tour by going back to respective depots
            for r in range(num_robots):
                tours[r].append(depot_cities[r])

            # Calculate fitness (total distance of all tours)
            tour_length = sum(sum(distance_matrix[tours[r][i]][tours[r][i+1]] for i in range(len(tours[r])-1)) for r in range(num_robots))
            if tour_length < best_tour_length:
                best_tour_length = tour_length
                best_solutions = tours

        # Update the pheromones
        for r in range(num_robots):
            for i in range(len(best_solutions[r])-1):
                for j in range(num_cities):
                    pheromone_matrix[best_solutions[r][i]][best_solutions[r][i+1]] *= (1-evaporation_rate)
                    pheromone_matrix[best_solutions[r][i]][best_solutions[r][i+1]] += pheromone_deposit

    return best_solutions, best_tour_length

def select_next_city(current_city, unvisited, pheromone_matrix, distance_matrix):
    probabilities = []
    for next_city in unvisited:
        if distance_matrix[current_city][next_city] > 0:
            pheromone = pheromone_matrix[current_city][next_city]**alpha
            heuristic = (1 / distance_matrix[current_city][next_city])**beta
            probabilities.append((next_city, pheromone * heuristic))

    if probabilities:
        next_city = random.choices([p[0] for p in probabilities], weights=[p[1] for p in probabilities], k=1)[0]
        return next_city
    return None

# Run ACO
best_solution, overall_cost = aco_for_mTSP(num_robots, depot_cities)

# Output the best solution and cost
for robot, tour in enumerate(best_solution):
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))}")
print(f"Overall Total Travel Cost: {overall_cost}")