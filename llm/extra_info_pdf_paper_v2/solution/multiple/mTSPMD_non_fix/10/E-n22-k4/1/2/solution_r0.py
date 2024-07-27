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

# Split cities among robots, naive assignment (not optimized)
def split_cities(n_cities, n_robots):
    return np.array_split(range(n_cities), n_robots)

def simulated_annealing(tour, start_temp, cool_rate, max_iter):
    current_temp = start_temp
    current_tour = tour[:]
    current_cost = sum(distance(current_tour[i-1], current_tour[i]) for i in range(len(current_tour)))
    
    for iteration in range(max_iter):
        i, j = np.random.choice(range(1, len(tour) - 1), 2, replace=False)
        test_tour = current_tour[:]
        test_tour[i], test_tour[j] = test_tour[j], test_tour[i]
        test_cost = sum(distance(test_tour[k-1], test_tour[k]) for k in range(len(test_tour)))
        
        if test_cost < current_cost or np.random.rand() < np.exp((current_cost - test_cost) / current_temp):
            current_tour = test_tour[:]
            current_cost = test_cost
        
        current_temp *= cool_rate
    
    return current_tour, current_cost

# Main execution
robots = 4
cities_per_robot = split_cities(len(coordinates), robots)
initial_temp = 1000
cooling_rate = 0.995
iterations = 10000

tour_results = []
total_cost = 0

for i in range(robots):
    start_city = depots[i]
    cities = list(cities_per_robot[i])
    if start_city not in cities:
        cities.append(start_city)
    tour, cost = simulated_annealing(cities, initial_temp, cooling_rate, iterations)
    tour_results.append((i, tour, cost))
    total_cost += cost

# Display the final results
for robot_id, tour, cost in tour_results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
    
print(f"Overall Total Travel Cost: {total_tcost:.2f}")