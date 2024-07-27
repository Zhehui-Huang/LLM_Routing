import math
from operator import itemgetter

# Define data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8,
    7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40
depot = 0

# Calculate distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate initial savings list
def calculate_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(1, len(coordinates)):
            if i != j:
                sij = (euclidean_distance(coordinates[depot], coordinates[i]) +
                       euclidean_distance(coordinates[depot], coordinates[j]) -
                       euclidean_distance(coordinates[i], coordinates[j]))
                savings.append((i, j, sij))
    savings.sort(key=itemgetter(2), reverse=True)
    return savings

# Initialize tours
def initialize_tours():
    tours = {[0, i, 0]: demands[i] for i in range(1, len(demands)) if demands[i] > 0}
    return tours

# Attempt to merge tours
def merge_tours(tours, merge_candidates):
    while merge_candidates:
        i, j, _ = merge_candidates.pop(0)
        merged = False
        for keyi in list(tours):
            if merged:
                break
            for keyj in list(tours):
                if keyi != keyj and j in keyi and i in keyj:
                    if tours[keyi] + tours[keyj] <= robot_capacity:
                        # Merging tours
                        new_tour = keyi[:-1] + keyj[1:]  # remove redundant depot
                        tours[new_tour] = tours.pop(keyi) + tours.pop(keyj)
                        merged = True
                        break
        if not merged:
            break  # No more mergeable tours under current constraints
    return tours

# Calculate tour costs
def calculate_tour_costs(tours):
    tour_costs = {}
    for tour in tours:
        cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        tour_costs[tour] = cost
    return tour_costs

# Solution formation
def solve_cvrp():
    savings = calculate_savings()
    tours = initialize_tours()
    tours = merge_tours(tours, savings)
    tour_costs = calculate_tour_costs(tours)
    
    total_cost = sum(tour_costs.values())
    for index, (tour, cost) in enumerate(tour_costs.items()):
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

solve_cvrp()