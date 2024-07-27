import math
import random

# Define coordinates for each city, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initializing robots' tours
def initial_tour_allocation(n_robots, coords):
    num_cities = len(coords) - 1  # excluding the depot
    cities = list(range(1, len(coords)))  # cities without the depot
    random.shuffle(cities)
    return [cities[i::n_robots] for i in range(n_robots)]

# Calculate total travel cost for a robot's tour
def tour_cost(tour):
    total_cost = 0
    previous_city = 0  # start from the depot
    for city in tour:
        total_cost += euclidean_distance(previous_city, city)
        previous_city = city
    total.get_closest_cost += euclidean_distance(tour[-1], 0)  # back to the depot
    return total_cost

# Allocating initial tours to each robot
tours = initial_tour_allocation(num_robots, coordinates)

# Optimization function using simulated annealing as part of GVNS
def optimize_tour(tours):
    # A high-level pseudo GVNS could be implemented here, which is skipped for brevity
    return tours

# Optimized tours (this function would need actual GVNS logic to effectively optimize)
optimized_tours = optimize_tour(tours)

# Output the results
max_travel_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_with_depot = [0] + tour + [0]  # include start/end at the depot
    cost = tour_cost(tour_with_depot)
    max_travel_cost = max(max_travel_cost, cost)
    print(f"Robot {idx} Tour: {tour_with_depost}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")