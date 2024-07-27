import math
import random

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots
num_robots = 8
# All robots start at depot 0
start_depot = 0

# Compute distances matrix
distances = [[math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2) 
              for j in range(len(coords))] for i in range(len(coords))]

def total_cost(tours):
    cost = 0
    for tour in tours:
        tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        cost += tour_cost
    return cost

# Initialize robot tours randomly
tours = [[] for _ in range(num_robots)]
remaining_cities = list(range(1, len(coords)))  # Exclude the initial depot

for city in remaining_cities:
    chosen_robot = random.choice(range(num_robots))
    tours[chosen_robot].append(city)

# Add depot to start and end of each tour
for tour in tours:
    tour.insert(0, start_depot)
    tour.append(start_depot)

# Simulated Annealing parameters
temp = 1000
cooling_rate = 0.995
min_temp = 1

while temp > min_temp:
    old_cost = total_cost(tours)
    # Perturb solution
    robot_idx = random.randint(0, num_robots - 1)
    tour = tours[robot_idx]
    if len(tour) > 2:
        # Swap two cities in the tour
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[i], tour[j] = tour[j], tour[i]
        # Evaluate new cost
        new_cost = total_cost(tours)
        # Acceptance probability
        if new_cost < old_cost or random.random() < math.exp((old_cost - new_cost) / temp):
            old_cost = new_cost
        else:
            # Reject the change
            tour[i], tour[j] = tour[j], tour[i]
    temp *= cooling_rate

# Output the results
overall_cost = total_cost(tours)
for idx, tour in enumerate(tours):
    robot_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")