import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize tours for each robot
def initialize_tours(num_robots, num_cities):
    city_list = list(range(2, num_cities))  # exclude depots already assigned as start
    random.shuffle(city_list)
    # Evenly distribute cities among robots as starting point
    avg = len(city_list) / float(num_robots)
    tours = []
    last = 0.0
    while last < len(city_list):
        tours.append(city_list[int(last):int(last + avg)])
        last += avg
    for i, tour in enumerate(tours):
        tours[i].insert(0, 0)  # start at depot 0
    return tours

# Simulated Annealing to optimize each tour
def simulated_annealing(tours, initial_temp, cooling_rate, num_iterations):
    def cost(tour):
        return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    for temp in range(num_iterations):
        for k in range(len(tours)):
            current_cost = cost(tours[k])
            i, j = sorted(random.sample(range(1, len(tours[k])), 2))
            new_tour = tours[k][:i] + tours[k][i:j][::-1] + tours[k][j:]
            new_cost = cost(new_tour)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / (initial_temp * cooling_rate ** temp)):
                tours[k] = new_tour
    return tours

# Parameters
num_robots = 2
num_cities = len(cities)
initial_temp = 10.0
cooling_rate = 0.95
num_iterations = 1000

# Initial tours
tours = initialize_tours(num_robots, num_cities)
# Optimize tours
optimized_tours = simulated_annealing(tours, initial_temp, cooling_rate, num_iterations)

# Calculate the cost and prepare the output
total_travel_cost = 0
final_tours = []

for i, tour in enumerate(optimized_tours):
    tour_cost = sum(distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
    total_travel_cost += tour_cost
    final_tours.append((tour + [tour[-1]], tour_cost))  # Append ending city

# Output results
for i, (tour, cost) in enumerate(final_tours):
    print(f"Robot {i} Tour: {' -> '.join(map(str, tour))}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")