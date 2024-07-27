import random
import math
from copy import deepcopy

# Constants
NUM_CITIES = 22
NUM_ROBOTS = 4
DEPOTS = [0, 0, 0, 0]  # All robots start at depot city 0

# Cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def create_tour_permutations():
    all_cities = list(cities.keys())[1:]  # exclude the depot from the permutations
    segments = random.sample(all_cities, len(all_cities))
    allocated_segments = [segments[i::NUM_ROBOTS] for i in range(NUM_ROBOTS)]
    tours = [[0] + seg + [0] for seg in allocated_segments]  # add the depot at the beginning and end
    return tours

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def solve_tsp_vrp():
    best_tours = create_tour_permutations()
    total_cost = 0
    results = []
    
    for robot_id, tour in enumerate(best_tours):
        cost = total_tour_cost(tour)
        total_cost += cost
        results.append((robot_id, tour, cost))
    
    return results, total_cost

# Running the TSP VRP Solver
results, overall_total_cost = solve_tsp_vrp()
for result in results:
    robot_id, tour, cost = result
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")