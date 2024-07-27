import random
import math
from itertools import permutations

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find a possible solution by assigning roughly half of the cities to each robot
# and then finding a reasonable path through each subset using permutations.
# Note: We use permutations exhaustively here for demonstration which is not practical for larger sizes.
def find_solution():
    city_indices = list(range(1, len(coordinates)))
    best_score = float('inf')
    best_routes = None

    for division in permutations(city_indices, len(city_indices)//2):
        robot_1_cities = list(division)
        robot_2_cities = [city for city in city_indices if city not in robot_1_cities]
        robot_1_tour = [0] + robot_1_cities + [0]
        robot_2_tour = [0] + robot_2_cities + [0]

        # Calculate cost
        cost1 = sum(calculate_distance(robot_1_tour[i], robot_1_tour[i+1]) for i in range(len(robot_1_tour)-1))
        cost2 = sum(calculate_distance(robot_2_tour[i], robot_2_tour[i+1]) for i in range(len(robot_2_tour)-1))
        total_cost = cost1 + cost2

        if total_cost < best_score:
            best_score = total_cost
            best_routes = (robot_1_tour, cost1, robot_2_tour, cost2)

    return best_routes, best_score

# Running the solution finder
(best_routes, best_score) = find_solution()
robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost = best_routes

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost:.2f}")

print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost:.2f}")

print(f"Overall Total Travel Cost: {best_score:.2f}")