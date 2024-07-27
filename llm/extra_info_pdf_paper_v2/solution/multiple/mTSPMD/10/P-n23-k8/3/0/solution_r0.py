import numpy as np
from scipy.spatial import distance_matrix

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Distance matrix calculation
dist_matrix = distance_matrix(coordinates, coordinates)

# Ant Colony Optimization parameters
num_ants = 10
num_iterations = 100
decay = 0.75
alpha = 1
beta = 4
Q = 500

# Initializes pheromones
pheromones = np.ones((len(coordinates), len(coordinates))) * 0.1

# Robot information
depots = list(range(8))
robots = len(depots)
ant_solutions = []

def aco_multi_depot_tsp():
    global pheromones

    for iteration in range(num_iterations):
        routes = []
        for ant in range(num_ants):
            routes.append(create_route())
        
        pheromones *= decay  # Evaporation
        
        # Pheromone update based on best solutions
        shortest_tour = min(routes, key=lambda x: x[1])
        for i, (from_city, to_city) in enumerate(zip(shortest_tour[0], shortest_tour[0][1:])):
            pheromones[from_city][to_city] += Q / shortest_tour[1]
            
    return shortest_tour
        
def create_route():
    routes = {r: [r] for r in depots}
    unvisited_cities = set(range(len(coordinates))) - set(depots)
    
    while unvisited_cities:
        for r in depots:
            if not unvisited_cities:
                break
            next_city = select_city(routes[r][-1], unvisited_cities)
            unvisited_cities.remove(next_city)
            routes[r].append(next_city)
    
    # Closing the tours at their respective depots
    for r in depots:
        routes[r].append(r)
    
    total_cost = sum(dist_matrix[routes[r][-2]][r] for r in depots)
    return routes, total_cost

def select_city(current_city, unvisited_cities):
    probabilities = []
    for city in unvisited_cities:
        trail = pheromones[current_city][city] ** alpha
        visibility = (1.0 / dist_matrix[current_city][city]) ** beta
        probabilities.append(trail * visibility)
    probabilities = np.array(probabilities) / sum(probabilities)
    next_city = np.random.choice(list(unvisited_cities), p=probabilities)
    return next_city

# Running the ACO algorithm
best_solution = aco_multi_depot_tsp()

# Presenting the results
print("Results:")
overall_total_cost = 0
for robot, tour in best_solution[0].items():
    robot_tour_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_cost += robot_tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")