import math
import random

# Define the coordinates of all cities, including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Simulated Annealing algorithm to solve the touring problem
def simulated_annealing(cities):
    N = len(cities)
    tour = list(range(N))
    for i in range(N):
        if i < 7:  # ensuring robots start at a depot
            tour[i] = i
        else:
            tour[i] = (i + 7) % N if i + 7 < N else (i + 7) % N + 1

    def cost(tour):
        return sum(distance(cities[tour[i]], cities[tour[(i + 1) % N]]) for i in range(N))

    old_cost = cost(tour)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        new_tour = tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = cost(new_tour)
        delta = new_cost - old_cost
        if delta < 0 or math.exp(-delta / T) > random.random():
            tour = new_tour
            old_cost = new_cost
        T *= alpha

    return tour, old_cost

# Assuming each robot starts at depot city 0
num_robots = 8
assignment = [[] for _ in range(num_robots)]
tour, total_cost = simulated_annealing(cities)

# Assigning cities to robots almost equally
cities_per_robot = len(tour) // num_robots
start = 0
for i in range(num_robots):
    end = start + cities_per_robot + (1 if i < len(tour) % num_robots else 0)
    assignment[i] = tour[start:end]
    start = end

for i in range(num_robots):
    print(f"Robot {i} Tour: {[0] + assignment[i]}")
    robot_tour_cost = sum(distance(cities[assignment[i][j]], cities[assignment[i][(j + 1) % len(assignment[i])]]) for j in range(len(assignment[i])))
    print(f"Robot {i} Total Travel Cost: {robot_tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")