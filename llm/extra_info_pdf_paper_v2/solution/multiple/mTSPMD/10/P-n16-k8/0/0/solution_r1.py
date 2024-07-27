import numpy as np

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Parameters
num_ants = 8  # This equals the number of robots and depots.
num_iterations = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromone_deposit_weight = 1.0

# Distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
        else:
            distance_matrix[i, j] = float('inf')

# Initialize pheromone matrix
pheromone_matrix = np.ones((num_cities, num_cities)) * 0.1

# Visibility matrix (inverse of distance)
visibility_matrix = 1 / distance_matrix

def ant_colony_optimization():
    global pheromone_matrix
    best_cost = float('inf')
    best_solution = []

    for iteration in range(num_iterations):
        routes = []
        costs = np.zeros(num_ants)
        for ant in range(num_ants):
            start_city = ant  # start at depot city indexed by robot number
            tour = [start_city]
            visited = set(tour)
            
            current_city = start_city
            while len(visited) < num_cities:
                probabilities = (pheromone_matrix[current_city] ** alpha) * (visibility_matrix[current_city] ** beta)
                probabilities[visited] = 0  # set probabilities of visited cities to zero
                probabilities /= probabilities.sum()
                
                next_city = np.random.choice(num_cities, p=probabilities)
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city

            tour.append(start_city)  # return to the starting depot
            routes.append(tour)

            # Calculate the cost of the tour
            tour_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
            costs[ant] = tour_cost

        # Update pheromones
        pheromone_matrix *= (1 - evaporation_rate)  # Evaporation
        for ant in range(num_ants):
            for i in range(len(routes[ant]) - 1):
                pheromone_matrix[routes[ant][i], routes[ant][i+1]] += pheromone_deposit_weight / costs[ant]

        # Check best solution
        current_iteration_cost = costs.sum()
        if current_iteration_cost < best_cost:
            best_cost = current_iteration_cost
            best_solution = routes

    return best_solution, best_cost

# Run optimization
optimized_routes, optimized_cost = ant_colony_optimization()

# Display results
print(f"Overall Total Travel Cost: {optimized_cost:.2f}")
for idx, route in enumerate(optimized_routes):
    route_cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")