import numpy as as np
import itertools

# Euclidean distance helper
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize cities and coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Initialize depot city indices
depot_0 = 0
depot_1 = 1

# Calculate distances matrix
num_cities = len(city_coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Algorithm setup
num_robots = 2
pheromone = np.full((num_cities, num_cities), 0.1)
desirability = 1 / (1 + distances)  # Inverse of distance
evaporation_rate = 0.1
intensity = 1

# ACO process
for iteration in range(100):  # Iterate 100 times
    all_tours = []
    all_costs = []
    for robot in range(num_robots):
        tour = [depot_0 if robot == 0 else depot_1]
        unvisited = set(range(num_cities)) - {tour[0]}
        while unvisited:
            current = tour[-1]
            probabilities = [(pheromone[current, next_city] ** 1) * (desirability[current, next_city] ** 2) 
                             for next_city in unvisited]
            probabilities /= np.sum(probabilities)
            next_city = np.random.choice(list(unvisited), p=probabilities)
            tour.append(next_city)
            unvisited.remove(next_city)
        tour.append(tour[0])  # Return to the depot
        all_tours.append(tour)
        cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        all_costs.append(cost)

        # Update pheromone
        for i in range(len(tour) - 1):
            pheromone[tour[i], tour[i + 1]] += intensity / cost

    # Pheromone evaporation
    pheromone *= (1 - evaporation_range)

# Select the best tours based on cost
best_index = np.argmin(all_costs)
best_tours = all_tours[best_index]
best_costs = all_costs[best_instdex]

# Printing outputs as required
for i in range(num_robots):
    print(f"Robot {i} Tour: {all_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {all_costs[i]}")
print(f"Overall Total Travel Cost: {sum(all_costs)}")