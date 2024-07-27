import math
import random
from itertools import islice

# Cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Simulated Annealing parameters
temp = 10000
cooling_rate = 0.995
min_temp = 1

# Function for the simulated annealing process
def simulated_annealing(tour):
    current_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    temp = 10000

    while temp > min_temp:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
        new_cost = sum(distance(new_tour[i], new_tour[i+1]) for i in range(len(new_tour) - 1))

        if (new_cost < current_cost or
            random.uniform(0, 1) < math.exp((current ,temp - new_cost) / temp)):
            tour, current_cost = new_tour, new_cost
        temp *= cooling_rate

    return tour, current_cost

# Create initial tours for two robots
robot_tours = {
    0: [0] + random.sample(range(2, 11), 9) + [0],
    1: [1] + random.sample(range(11, 21), 10) + [1]
}

# Perform simulated annealing for each robot's tour
results = {}
total_cost = 0

for robot_id, tour in robot_tours.items():
    optimized_tour, tour_cost = simulated_annealing(tour)
    results[robot_id] = (optimized_tour, tour_cost)
    total_cost += tour_cost

# Output results for the required format
for robot_id, result in results.items():
    print(f"Robot {robot_id} Tour: {result[0]}")
    print(f"Robot {robot_id} Total Travel Cost: {result[1]}")

print(f"Overall Total Travel Cost: {total_cost}")