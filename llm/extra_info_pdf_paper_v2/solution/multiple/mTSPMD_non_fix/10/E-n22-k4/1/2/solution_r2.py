import numpy as np
import math

# Coordinates of all cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initial naive assignments of cities to every robot
def split_cities(n_cities, n_robots):
    return np.array_split(range(4, n_cities), n_robots)

def simulated_annealing(tour, start_temp, cool_rate, max_iter):
    current_temp = start_temp
    current_tour = tour[:]
    current_cost = sum(distance(current_tour[i], current_tour[i-1]) for i in range(1, len(current_tour)))
    n = len(tour)
    
    for iteration in range(max_iter):
        # Swap two cities
        i, j = np.random.choice(range(1, n), 2, replace=False)
        test_tour = current_tour[:]
        test_tour[i], test_tour[j] = test_tour[j], test_tour[i]
        test_cost = sum(distance(test_tour[k], test_tour[k-1]) for k in range(1, n))
        
        # Decide to accept the new tour if it's better or with a certain probability based on the temperature
        if test_cost < current_cost or math.exp((current_cost - test_cost) / current_temp) > np.random.rand():
            current_tour = test_tour[:]
            current_cost = test_cost
        
        # Reduce temperature
        current_temp *= cool_rate
    
    return current_tour, current_cost

robots = 4
total_cost = 0
initial_temp = 1000
cooling_rate = 0.995
iterations = 5000

city_groups = split_cities(len(coordinates), robots)
tour_results = []

# Calculate optimized tour for each robot starting from each depot
for i in range(robots):
    cities = [depots[i]] + list(city_groups[i])  # Adding depot to the start of the list
    tour, cost = simulated_annealing(cities, initial_temp, cooling_rate, iterations)
    tour_results.append(tour)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")