import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate distances between each pair of cities
distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Number of robots
num_robots = 4

# Solver function
def tsp_solver(cities, num_robots, distances):
    # Heuristic to assign cities to robots
    unassigned_cities = list(cities.keys())[1:]  # Excluding depot city 0
    robots_tours = {i: [0] for i in range(num_robots)}  # start each tour at the depot

    # Greedy assignment of cities to robots based on minimal incremental cost
    while unassigned_cities:
        for robot in range(num_robots):
            if not unassigned_cities:
                break
            min_cost = float('inf')
            best_city = None
            last_city = robots_tours[robot][-1]
            for city in unassigned_cities:
                cost = distances[(last_city, city)]
                if cost < min_cost:
                    min_cost = cost
                    best_city = city
            robots_tours[robot].append(best_city)
            unassigned_cities.remove(best_city)
    
    # Close each robot's tour at the depot
    for robot in range(num_robots):
        robots_tours[robot].append(0)

    # Calculate tour costs
    tour_costs = {}
    for robot in range(num_robots):
        tour_cost = sum(distances[(robots_tours[robot][i], robots_tours[robot][i + 1])] for i in range(len(robots_tours[robot]) - 1))
        tour_costs[robot] = tour_cost
        print(f"Robot {robot} Tour: {robots_tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {tour_cost}")

    # Determine maximum travel cost
    max_travel_cost = max(tour_costs.values())
    print(f"Maximum Travel Cost: {max_travel_cost}")

# Call the solver
tsp_solver(cities, num_robots, distances)