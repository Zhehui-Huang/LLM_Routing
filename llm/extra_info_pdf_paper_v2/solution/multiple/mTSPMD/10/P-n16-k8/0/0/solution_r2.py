import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Parameters
num_robots = 8
iterations = 200
alpha = 1.0   # Importance of pheromone
beta = 5.0    # Importance of heuristic (inverse of distance)
evaporation = 0.5
deposit = 1.0

# Distance function
def distance(i, j):
    return np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Initialize pheromone levels
num_cities = len(cities)
pheromone = np.ones((num_cities, num_cities))
visibility = np.array([[1 / (distance(i, j) if i != j else float('inf')) for j in range(num_cities)] for i in range(num_cities)])

# Initialize tours matrix
best_routes = None
best_cost = float('inf')


def ant_colony_optimization():
    global best_routes, best_cost
    for _ in range(iterations):
        routes = []
        costs = []
        
        for robot in range(num_robots):
            # Start at each depot for each robot
            start_city = robot
            route = [start_city]
            unvisited = set(range(num_cities)) - set(route)

            current_city = start_city
            while unvisited:
                probabilities = [pheromone[current_city][j]**alpha * visibility[current_city][j]**beta if j in unvisited else 0 for j in range(num_cities)]
                probabilities_sum = sum(probabilities)
                probabilities = [p / probabilities_sum for p in probabilities]
                
                next_city = random.choices(population=list(range(num_cities)), weights=probabilities, k=1)[0]
                route.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city

            route.append(start_city)  # Return to depot
            routes.append(route)
        
            # Calculate cost of the route
            route_cost = sum([distance(route[i], route[i+1]) for i in range(len(route)-1)])
            costs.append(route_cost)

        # Update pheromones
        for route, cost in zip(routes, costs):
            for i in range(len(route) - 1):
                pheromone[route[i]][route[i+1]] += deposit / cost

        pheromone *= (1 - evaporation)  # Evaporation

        total_cost = sum(costs)
        if total_cost < best_cost:
            best_cost = total_cost
            best_routes = routes

ant_colony_optimization()

# Display results
overall_cost = 0
for idx, route in enumerate(best_routes):
    route_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    overall_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")