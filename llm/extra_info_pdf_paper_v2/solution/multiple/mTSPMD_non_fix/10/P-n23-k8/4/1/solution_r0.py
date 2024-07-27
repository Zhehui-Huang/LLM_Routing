import math
import random

# Define the coordinates of all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Assign each robot to the starting depot city 0
depots = [0] * num_robots

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calc_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

def simulated_annealing(initial_state, temp, cool, min_temp):
    current_state = initial_state.copy()
    current_cost = calc_tour_cost(current_state)
    best_state = current_state
    best_cost = current_cost

    while temp > min_temp:
        next_state = current_state.copy()
        # Swap two cities to generate neighbor state
        i1, i2 = random.sample(range(1, len(next_state)), 2)  # exclude starting depot
        next_state[i1], next_state[i2] = next_state[i2], next_state[i1]
        next_cost = calc_tour_cost(next_state)
        
        # If the new solution is better, accept it
        # If it's worse, maybe accept it
        if next_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - next_cost) / temp):
            current_state = next_state
            current_cost = next_cost
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
        
        temp *= cool  # Cool down

    return best_state, best_cost

# Divide cities among robots evenly, each robot includes the depot at start
cities_per_robot = len(coordinates) // num_robots
assignments = [list(range(i * cities_per_robot + 1, (i + 1) * cities_per_robot + 1)) for i in range(num_robots)]
for i, a in enumerate(assignments):
    a.insert(0, depots[i])  # add starting depot at the beginning

# Applying simulated annealing to find tours for each robot
tours = []
costs = []
overall_cost = 0
for tour in assignments:
    final_tour, tour_cost = simulated_annealing(tour, 1000, 0.99, 1)
    tours.append(final_tour)
    costs.append(tour_cost)
    overall_cost += tour_cost

for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")