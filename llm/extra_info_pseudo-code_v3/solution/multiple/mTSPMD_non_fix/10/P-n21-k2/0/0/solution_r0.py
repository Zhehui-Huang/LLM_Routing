import math
import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Define depots
depots = [0, 1]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to create the initial tour using the nearest neighborhood search
def nearest_neighbor_tour(depot, cities_list):
    tour = [depot]
    current = depot
    while cities_list:
        next_city = min(cities_list, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        cities_list.remove(next_city)
        current = next_city
    return tour

# Applying the NNS heuristic algorithm
non_depot_cities = list(set(cities.keys()) - set(depots))

# Randomly assign non-depot cities to two depots initially
np.random.shuffle(non_depot_cities)
split = len(non_depot_cities) // 2
assigned_cities = [non_depot_cities[:split], non_depot_cities[split:]]

# Generate starting tours for each robot
tours = [nearest_neighbor_tour(depots[i], assigned_cities[i]) for i in range(2)]

# Tabu Search parameters
max_iterations = 1000
tabu_list = {}
iteration = 0
no_improve = 0
best_tours = tours
best_cost = float('inf')

# Function to calculate the cost of tours
def tour_cost(tours):
    cost_sum = 0
    robot_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        robot_costs.append(cost)
        cost_sum += cost
    return cost_sum, robot_costs

# Main Tabu Search Loop
while iteration < max_iterations and no_improve < 200:
    # Perform moves (relocate, exchange, tail-swap) and calculate cost
    # Update tours if better and not in tabu list
    # Simplified example of trying a random relocate operation
    if random.random() < 0.5:  # random choice to either attempt a relocate or exchange
        tour_id, city_idx = random.choice([(tid, cid) for tid, t in enumerate(tours) for cid in range(len(t))])
        target_tour_id = 1 - tour_id
        city_to_move = tours[tour_id].pop(city_idx)
        insert_position = random.randint(1, len(tours[target_tour_id]) - 1)
        tours[target_tour_id].insert(insert_position, city_to_move)
    else:  # attempt a simple 2-opt within a tour
        tour_id = random.choice([0, 1])
        i, j = sorted(random.sample(range(1, len(tours[tour_count]) - 2), 2))
        tours[tour_id][i:j] = reversed(tours[tour_id][i:j])
    
    current_cost, robot_costs = tour_cost(tours)
    if current_cost < best_cost and str(tours) not in tabu_list:
        best_tours = [list(t) for t in tours]
        best_cost = current_cost
        tabu_list[str(tours)] = 10  # adding a simple tabu duration
        no_improve = 0
    else:
        no_improve += 1

    # Update tabu list
    for key in list(tabu_list.keys()):
        tabu_list[key] -= 1
        if tabu_list[key] <= 0:
            del tabu_list[key]

    iteration += 1

# Return the optimal tours and total travel cost
overall_cost, individual_costs = tour_cost(best_tours)
print("Optimal Tours and Costs")
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")
print(f"Overall Total Travel Cost: {overall_Cost}")