import random
import numpy as np

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8
# Depots
depots = list(range(num_robots))

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize pheromone levels
pheromones = [[1 for _ in cities] for _ in cities]
n_cities = len(cities)

# Ant Colony Optimization parameters
alpha = 1.0  # Influence of pheromone
beta = 2.0   # Influence of heuristic information (1/distance)
evaporation_rate = 0.5
n_iterations = 50
n_ants = 25

def ant_colony_optimization():
    best_tours = []
    best_cost = float('inf')
    
    for iteration in range(n_iterations):
        all_tours = []
        all_costs = []
        for ant in range(n_ants):
            tours = []
            costs = []
            remaining_cities = set(cities.keys()) - set(depots)
            for depot in depots:
                robot_tour = [depot]
                current_city = depot
                tour_cost = 0

                while remaining_cities:
                    probabilities = []
                    sum_probabilities = 0
                    for city in remaining_cities:
                        prob = ((pheromones[current_city][city] ** alpha) *
                                ((1 / distance(current_city, city)) ** beta))
                        probabilities.append(prob)
                        sum_probabilities += prob

                    if sum_probabilities == 0:
                        probabilities = [1 for _ in remaining_cities]
                        sum_probabilities = sum(probabilities)
                    
                    probabilities = [p / sum_probabilities for p in probabilities]
                    next_city = random.choices(list(remaining_cities), probabilities)[0]
                    robot_tour.append(next_city)
                    tour_cost += distance(current_city, next_city)
                    current_city = next_city
                    remaining_cities.remove(next_city)
                
                robot_tour.append(depot)
                tour_cost += distance(current_city, depot)  # Return to depot
                tours.append(robot_tour)
                costs.append(tour_cost)

            all_tours.append(tours)
            all_costs.append(costs)

        # Update best solution
        for tours, costs in zip(all_tours, all_costs):
            total_cost = sum(costs)
            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = tours

        # Update pheromones
        for i in range(n_cities):
            for j in range(n_cities):
                pheromones[i][j] *= (1 - evaporation_rate)

        for tours, costs in zip(all_tours, all_costs):
            for tour, cost in zip(tours, costs):
                for k in range(len(tour) - 1):
                    i, j = tour[k], tour[k+1]
                    pheromones[i][j] += 1 / cost
    
    return best_tours, best_cost

# Run the ACO algorithm
best_tours, best_cost = ant_colony_optimization()

# Output format adaptation
overall_total_cost = 0
for idx, (tour, cost) in enumerate(zip(best_tours, [distance(tour[i], tour[i+1]) for tour in best_tours for i in range(len(tour)-1)])):
    robot_tour_cost = sum(cost)
    overall_total_cost += robot_tour_tcost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {robot_tour_total}")

print(f"Overall Total Travel Cost: {overall_total_cost}")