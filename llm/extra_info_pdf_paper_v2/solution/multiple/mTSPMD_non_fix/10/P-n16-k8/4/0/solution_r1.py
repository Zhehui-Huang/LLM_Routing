import random
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initial random solution distributing cities almost evenly among robots
NUM_ROBOTS = 8
robots_routes = {i: [0] for i in range(NUM_ROBOTS)}  # start each robot's route at depot city 0
remaining_cities = list(cities.keys())[1:]  # exclude the initial depot
random.shuffle(remaining_cities)

chunk_size = len(remaining_cities) // NUM_ROBOTS
chunks = [remaining_cities[i:i + chunk_size] for i in range(0, len(remaining_cities), chunk_size)]

for i in range(NUM_ROBOTS):
    if i < len(chunks):
        robots_routes[i] += chunks[i]

# Simulated Annealing to optimize routes
T = 10000
cooling_rate = 0.995
min_temperature = 1

def calculate_total_distance(route):
    return sum(euclidean_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

while T > min_temperature:
    for _ in range(100):  # Number of trials at each temperature step
        # Generating new candidate by swapping nodes between two routes
        r1, r2 = random.sample(list(robots_routes.keys()), 2)
        if len(robots_routes[r1]) > 1 and len(robots_routes[r2]) > 1:
            i1, i2 = random.randint(1, len(robots_routes[r1]) - 1), random.randint(1, len(robots_routes[r2]) - 1)
            robots_routes[r1][i1], robots_routes[r2][i2] = robots_routes[r2][i2], robots_routes[r1][i1]

            # Calculate new costs to decide if we should accept new solution
            new_cost_r1 = calculate_total_distance(robots_routes[r1])
            new_cost_r2 = calculate_total_distance(robots_routes[r2])
            current_cost_r1 = calculate_total_distance(robots_routes[r1][:i1] + [robots_routes[r1][i1]] + robots_routes[r1][i1 + 1:])
            current_cost_r2 = calculate_total_distance(robots_routes[r2][:i2] + [robots_routes[r2][i2]] + robots_routes[r2][i2 + 1:])

            if new_cost_r1 + new_cost_r2 < current_cost_r1 + current_cost_r2 or random.random() < math.exp((current_cost_r1 + current_cost_r2 - new_cost_r1 - new_cost_r2) / T):
                continue

            # Revert swap if not accepted
            robots_routes[r1][i1], robots_routes[r2][i2] = robots_routes[r2][i2], robots_routes[r1][i1]

    T *= cooling_rate

# Calculate the final results
total_cost = 0
for i in range(NUM_ROBOTS):
    cost = calculate_total_distance(robots_routes[i])
    total_cost += cost
    print(f"Robot {i} Tour: {robots_routes[i]}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_opt_cost:.2f}")