import math
import random
import numpy as np

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robots info
num_robots = 8
starting_depot = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

# Simulated Annealing to optimize route
def simulated_annealing(tour, dist_matrix):
    n = len(tour)
    cost = lambda route: sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    current_cost = cost(tour)
    temp = 1000
    cooling_rate = 0.995
    while temp > 0.1:
        i, j = sorted(random.sample(range(1, n-1), 2))
        new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
        new_cost = cost(new_tour)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            tour, current_cost = new_tour, new_cost
        temp *= cooling_rate
    return tour, current_cost

dist_matrix = create_distance_matrix(cities)

# Divide the cities among the robots from the starting depot
city_ids = list(cities.keys())
city_ids.remove(starting_depot)
per_robot = len(city_ids) // num_robots
assignments = [city_ids[i:i + per_robot] for i in range(0, len(city_ids), per_robot)]

# Ensuring each robot starts and ends at the depot
tours = [[starting_depot] + assignment + [starting_depot] for assignment in assignments]

# Optimize each tour using simulated annealing
optimized_tours = []
total_cost = 0
for tour in tours:
    opt_tour, opt_cost = simulated_annealing(tour, dist_matrix)
    optimized_tours.append(opt_tour)
    total_cost += opt_cost

# Print the information as required
for index, tour in enumerate(optimized_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {opt_cost}")

print(f"Overall Total Travel Cost: {total_cost}")