import numpy as np

# Number of cities and Robots
n_cities = 22
n_robots = 4

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Start and end depots for each robot
depots = [0, 1, 2, 3]

# Calculating distance matrix
def euclidean_distance(coord1, coord2):
    return np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Ant Colony Optimization algorithm setup
def aco_algorithm(n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    best_cost = float('inf')
    best_solution = []

    # Initialize pheromones
    pheromones = np.ones((n_cities, n_cities)) * 0.1

    for iteration in range(n_iterations):
        all_solutions = []
        all_costs = []

        for ant in range(n_ants):
            # Each ant starts at the designated depot
            start_depot = depots[ant % n_robots]  # Cycle through depots for robots
            tour = [start_depot]
            current_city = start_depot

            while len(tour) < n_cities:
                # Probabilities for moving to the next city
                probabilities = []
                for city in range(n_cities):
                    if city not in tour:
                        prob = (pheromones[current_city][city] ** alpha) * ((1.0 / distance_matrix[current_city][city]) ** beta)
                        probabilities.append(prob)
                    else:
                        probabilities.append(0)
                probabilities /= np.sum(probabilities)

                # Select next city based on probabilities
                next_city = np.random.choice(range(n_cities), p=probabilities)
                tour.append(next_city)
                current_city = next_city
            
            # Return to start depot
            tour.append(start_depot)

            # Calculate the cost of the tour
            tour_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
            all_solutions.append(tour)
            all_costs.append(tour_cost)

            # Update the best solution if found
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_solution = tour

        # Update pheromones (evaporation and deposit)
        pheromones *= (1 - evaporation_rate)
        for tour, cost in zip(all_solutions, all_costs):
            deposit_amount = Q / cost
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += deposit_amount
                pheromones[tour[i+1]][tour[i]] += deposit_amount

    return best_solution, best_cost

# Run ACO
best_tour, best_tour_cost = aco_algorithm(n_ants=40, n_iterations=100, alpha=1, beta=5, evaporation_rate=0.1, Q=100)

# Printing the results
print("Best Tour:", best_tour)
print("Best Tour Cost:", best_tour_cost)