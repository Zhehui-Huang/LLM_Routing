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
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initial naive distribution of cities to the robots
def initial_distribution(cities, num_robots):
    num_cities = len(cities) - 1
    shuffled_cities = list(range(1, num_cities + 1))
    seed(42)
    shuffle(shuffled_cities)
    avg_cities_per_robot = num_cities // num_robots
    tours = []
    for i in range(num_robots):
        start_index = i * avg_cities_per_robot
        if i == num_robots - 1:
            assigned_cities = shuffled_cities[start_index:]
        else:
            assigned_cities = shuffled_cities[start_index:start_index + avg_cities_per_robot]
        tours.append([0] + assigned_cities + [0])
    return tours

# Calculate tour cost
def tour_cost(tour, city_locs):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(city_locs[tour[i]], city_locs[tour[i + 1]])
    return cost

# Initial tour distribution
initial_tours = initial_distribution(cities, 2)

# Optimize the tours (simple implementation)
def optimize_tours(tours, city_locs):
    best_tours = deepcopy(tours)
    min_max_cost = max(tour_cost(tour, city_locs) for tour in tours)
    
    for _ in range(10000):  # More iterations might be needed
        # A simple perturbation: swapping cities between first and second robot tours for optimization
        for swap_index_a in range(1, len(tours[0]) - 1):
            for swap_index_b in range(1, len(tours[1]) - 1):
                # Try swapping
                tours[0][swap_index_a], tours[1][swap_index_b] = tours[1][swap_index_b], tours[0][swapimaximumm_cost = max(tour_cost(tour, city_locs) for tour in tours)
                # Revert if didn't improve
                if maximum_cost >= min_max_cost:
                    tours[0][swap_index_a], tours[1][swap_index_b] = tours[1][swap_index_b], tours[0][swap_index_a]
                else:
                    min_max_cost = maximum_cost
                    best_tours = deepcopy(tours)

    return best_tours

optimized_tours = optimize_tours(initial_tours, cities)

# Output
print("Optimized Tours and Costs:")
max_cost = 0
for index, tour in enumerate(optimized_tours):
    cost = tour_cost(tour, cities)
    max_cost = max(max_cost, cost)
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")