import numpy as some.random
import random

# Initialization
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Euclidean distance calculation
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Parameters
num_cities = len(coordinates)
pheromone = np.ones((num_cities, num_cities))
desirability = np.reciprocal(np.array([[distance(i, j) if i != j else 1e10 for j in range(num_cities)] for i in range(num_cities)]))
total_ants = 40
iterations = 100
evaporation_rate = 0.1
alpha = 1  # Pheromone importance
beta = 5   # Distance importance

# Ant Colony Optimization implementation
def ant_colony_optimization():
    best_cost = float('inf')
    best_routes = None

    for _ in range(iterations):
        routes = [[0], [1]]
        costs = [0, 0]
        
        # Each ant builds a tour for both robots
        for ant in range(total_ants // 2):
            remaining_cities = set(range(2, num_cities))
            for depot_index in range(2):
                while remaining_cities:
                    current_city = routes[depot_index][-1]
                    probabilities = []
                    cumulative_prob = 0
                    
                    # Calculate probabilities for the next city
                    for city in remaining_cities:
                        probability = (pheromone[current_city][city]**alpha) * (desirability[current_city][city]**beta)
                        cumulative_prob += probability
                        probabilities.append((cumulative_prob, city))
                    
                    if cumulative_prob == 0:
                        break  # Prevent division by zero
                    
                    # Choose next city
                    pick = random.random() * cumulative_prob
                    next_city = next(city for prob, city in probabilities if prob > pick)
                    routes[depot_index].append(next_city)
                    costs[depot_index] += distance(current_city, next_city)
                    remaining_cities.remove(next_city)
                    
                # Complete tour returning to initial depot
                routes[depot_index].append(depot_index)
                costs[depot_index] += distance(routes[depot_index][-2], depot_index)
        
        # Update pheromones
        pheromone *= (1 - evaporation_rate)  # Evaporation
        for route in routes:
            for i in range(len(route) - 1):
                pheromone[route[i]][route[i+1]] += 1 / sum(costs)
                
        # Check if this solution is the best
        if sum(costs) < best_cost:
            best_cost = sum(costs)
            best_routes = routes

    return best_routes, best_cost

best_tours, best_cost = ant_colony_optimization()

# Output results
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")