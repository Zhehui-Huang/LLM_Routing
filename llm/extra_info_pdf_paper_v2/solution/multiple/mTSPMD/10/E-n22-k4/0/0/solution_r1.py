import numpy as np
import random

# Coordinates of all cities including the depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Depot assignments
depots = [0, 1, 2, 3]
num_robots = 4

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize distance matrix for all cities
n_cities = len(cities)
distances = np.array([[calculate_distance(i, j) for j in range(n_cities)] for i in range(n_cities)])

def initialize_ants(n_ants, num_robots):
    # Spread ants approximately equally across depots initially
    return [depots[i % num_robots] for i in range(n_ants)]

def ant_colony_optimization(n_ants=20, alpha=1.0, beta=5.0, evaporation_rate=0.5, iterations=100):
    # Pheromone matrix
    pheromone_matrix = np.ones((n_cities, n_cities)) * 0.1
    best_solution = [[], float('inf')]
    ants_starting_cities = initialize_ants(n_ants, num_robots)

    for _ in range(iterations):
        all_tours = []
        all_costs = []

        for ant in range(n_ants):
            start_city = ants_starting_cities[ant]
            tour = [start_city]
            unvisited = set(range(n_cities)) - {start_city}
            current_city = start_city

            while unvisited:
                probabilities = []
                for city in range(n_cities):
                    if city in unvisited:
                        trail = pheromone_matrix[current_city, city] ** alpha
                        desirability = (1.0 / distances[current_city, city]) ** beta
                        probabilities.append(trail * desirability)
                    else:
                        probabilities.append(0)
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(n_cities, p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city

            # Closing the tour by returning to the original depot
            tour.append(start_city)
            cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
            if cost < best_solution[1]:
                best_solution = [tour, cost]
            all_tours.append(tour)
            all_costs.append(cost)

        # Pheromone evaporation
        pheromone_matrix *= (1 - evaporation_rate)

        # Pheromone update
        for tour, cost in zip(all_tours, all_costs):
            for i in range(len(tour) - 1):
                pheromone_matrix[tour[i], tour[i + 1]] += 1 / cost

    return best_solution

# Get the best route from the ACS
best_tour, best_cost = ant_colony_optimization()

# Output result
print(f"Best Tour: {best_tour}")
print(f"Total Travel Cost: {best_cost}")