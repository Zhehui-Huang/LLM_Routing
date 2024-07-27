import math
from random import seed, shuffle
from copy import deepcopy

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initial naive distribution of cities to the robots
def initial_distribution(cities, num_robots):
    num_cities = len(cities) - 1
    shuffled_cities = list(range(1, num_cities + 1))
    seed(42) # For reproducibility
    shuffle(shuffled_cities)
    avg_cities_per_robot = num_cities // num_robots
    tours = []
    for i in range(num_robots):
        start_index = i * avg_cities_per_robot
        if i == num_robots - 1:
            assigned_cities = shuffled_cities[start_index:]
        else:
            assigned_cities = shuffled_cities[start_index:start_name_index + avg_cities_per_robot]
        tours.append([0] + assigned_cities + [0])
    return tours

# Calculate tour cost
def tour_cost(tour, city_locs):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(city_locs[tour[i]], city_locs[tour[i+1]])
    return cost

# Distribute tours initially
tours = initial_distribution(cities, 2)

# Simulated annealing or another local search to optimize tours here
def optimize_tours(tours, city_locs):
    best_tours = deepcopy(tours)
    min_max_cost = max(tour_cost(tour, city_locs) for tour in tours)
    
    for _ in range(1000):  # number of iterations
        new_tours = deepcopy(best_tours)
        # Here would be the logic to perturb the tours in a variable neighborhood search manner.
        # For simplicity, let's just switch one city from one tour to another and see if it improves.
        for i in range(len(new_tours)):
            for j in range(1, len(new_tours[i]) - 1):
                for k in range(len(new_tours)):
                    if i != k:
                        # Try moving new_tours[i][j] to tour k
                        new_city = new_tours[i].pop(j)
                        new_tours[k].insert(-1, new_city)
                        new_max_cost = max(tour_cost(tour, city_locs) for tour in new_tours)
                        if new_max_cost < min_max_cost:
                            min_max_cost = new_max_cost
                            best_tours = deepcopy(new_tours)
                        # Revert the move
                        new_tours[k].remove(new_city)
                        new_tours[i].insert(j, new_city)
    
    return best_tours

optimized_tours = optimize_tours(tours, cities)

# Calculate costs and display results
results = []
max_cost = 0
for index, tour in enumerate(optimized_tours):
    cost = tour_cost(tour, cities)
    results.append((tour, cost))
    max_cost = max(max_cost, cost)

print("Optimized Tours and Costs:")
for idx, result in enumerate(results):
    print(f"Robot {idx} Tour: {result[0]}")
    print(f"Robot {idx} Total Travel Cost: {result[1]:.2f}")
print(f"Maximum Travel Cost: {max_cost:.2f}")