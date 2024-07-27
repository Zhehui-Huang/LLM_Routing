from math import sqrt
from itertools import permutations

# Define the coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Define the number of robots and their respective depot start and end points
num_robots = 2
depots = [0, 1]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Brute force TSP solver for small sets of cities
def solve_tsp(tour_cities):
    min_tour = None
    min_cost = float('inf')
    for perm in permutations(tour_cities):
        cost = sum(calc_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))
        if cost < min_cost:
            min_cost = cost
            min_tour = perm
    return min_tour, min_cost

# Simple assignment of cities to robots
cities_per_robot = {
    0: list(range(1, 11)),  # robot 0 gets the first half, including its depot at the beginning
    1: list(range(11, 21))  # robot 1 gets the second half, including its depot at the beginning
}
cities_per_robot[0].append(0)  # end at its depot
cities_per_robot[1].append(1)  # end at its depot

total_cost = 0
all_tours = []

for robot_id, cities in cities_per_robot.items():
    tour, cost = solve_tsp(cities)
    all_tours.append((tour, cost))
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")