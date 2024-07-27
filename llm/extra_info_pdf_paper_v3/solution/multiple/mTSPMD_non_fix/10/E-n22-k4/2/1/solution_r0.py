import math
import random

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Calculate distance between two cities using Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots and their start cities (depots)
num_robots = 4
depots = [0, 1, 2, 3]

# Simulated Annealing parameters
temp = 10000
cooling_rate = 0.995
min_temp = 1

def simulated_annealing():
    # Initial solution: random allocation of cities to robots, excluding depots
    tours = {robot: [depot] for robot, depot in enumerate(depots)}
    remaining_cities = set(cities.keys()) - set(depots)
    for city in remaining_cities:
        chosen_robot = random.choice(list(tours.keys()))
        tours[chosen_robot].append(city)

    def tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i + 1])
        if len(tour) > 1:
            cost += distance(tour[-1], tour[0])  # Return to depot
        return cost

    def total_cost(tours):
        return sum(tour_cost(tour) for tour in tours.values())

    current_cost = total_cost(tours)

    while temp > min_temp:
        # Create new neighbor tour
        robot_id = random.choice(list(tours.keys()))
        current_tour = tours[robot_id]
        if len(current_tour) > 2:
            i, j = sorted(random.sample(range(1, len(current_tour)), 2))  # ignore depot for swapping
            new_tour = current_tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_cost(new_tour) + total_cost({k: v for k, v in tours.items() if k != robot_id})
            # Acceptance probability
            if new_cost < current_cost or math.exp((current_cost - new_cost) / temp) > random.random():
                tours[robot_id] = new_tour
                current_cost = new_cost

        temp *= cooling_rate

    return tours, current_cost

# Solve the MmTSP via Simulated Annealing
tours, total_travel_cost = simulated_annealing()

# Output results
for robot, tour in tours.items():
    robot_cost = tour_cost(tour)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")