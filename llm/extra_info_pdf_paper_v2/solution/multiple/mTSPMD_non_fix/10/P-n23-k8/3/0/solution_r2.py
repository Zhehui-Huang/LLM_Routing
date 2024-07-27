import random
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Calculate total tour cost
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour)))

# Simulated Annealing
def simulated_annealing(depot, cities, initial_temp=10000, cooling_rate=0.995, stopping_temp=1):
    cities = list(cities)
    current_temp = initial_temp
    current_solution = cities[:]
    random.shuffle(current_tour)
    best_tour = current_solution[:]
    best_cost = tour_cost(best_tour)

    while current_temp > stopping_temp:
        i, j = random.sample(range(1, len(cities)), 2)
        current_solution[i], current_solution[j] = current_solution[j], current_solution[i]
        current_cost = tour_cost(current_solution)
        if current_cost < best_cost or random.random() < math.exp((best_cost - current_cost) / current_temp):
            best_tour = current_solution[:]
            best_cost = current_cost
        current_temp *= cooling_rate

    return [depot] + best_tour  # Ensure starting at depot

# Distribute cities between robots
cities_per_robot = len(cities) // num_robots
additional_cities = len(cities) % num_robots
segments = [list(cities.keys())[i * cities_per_robot + min(i, additional_cities):(i + 1) * cities_per_robot + min(i + 1, additional_cities)] for i in range(num_robots)]

# Determine tours for each robot starting from depot city 0
tours = []
for i in range(num_robots):
    if segments[i]:
        tour = simulated_annealing(0, segments[i])
        tours.append(tour)
    else:
        tours.append([0])  # If no cities are assigned, stay at the depot

# Calculate costs
robot_costs = [tour_cost(tour) for tour in tours]
overall_cost = sum(robot_costs)

# Print results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print("Overall Total Travel Cost:", overall_cost)