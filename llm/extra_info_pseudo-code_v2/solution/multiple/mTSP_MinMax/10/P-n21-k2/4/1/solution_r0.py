import math
import random
from copy import deepcopy

# City coordinates, city 0 is the depot
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def initialize_tours(num_robots):
    sorted_cities = sorted(range(1, len(cities)), key=lambda x: euclidean_distance(0, x))
    tours = {i: [0] for i in range(num_robots)}
    for i, city in enumerate(sorted_cities):
        tours[i % num_robots].append(city)
    for tour in tours.values():
        tour.append(0)  # Return to depot
    return tours

def shake(tours, k):
    all_possible_tours = list(tours.keys())
    while k > 0:
        tour_id = random.choice(all_possible_tours)
        if len(tours[tour_id]) > 2:
            node_index = random.randint(1, len(tours[tour_id]) - 2)  # exclude depot
            node = tours[tour_id].pop(node_index)
            target_tour_id = random.choice([tid for tid in all_possible_tours if tid != tour_id])
            insert_position = random.randint(1, len(tours[target_tour_id]) - 1)
            tours[target_tour_id].insert(insert_position, node)
            k -= 1
    return tours

def seq_vnd(tours):
    # This simplified example only covers one-point moves between tours.
    improved = True
    while improved:
        improved = False
        for tour_id, tour in tours.items():
            for i in range(1, len(tour) - 1):
                for target_tour_id, target_tour in tours.items():
                    if tour_id != target_tour_id:
                        for j in range(1, len(target_tour) - 1):
                            # Try moving tour[i] to target_tour[j]
                            node = tour.pop(i)
                            target_tour.insert(j, node)
                            if cost_of_tours(tours) < current_cost:
                                improved = True
                                current_cost = cost_of_tours(tours)
                            else:
                                # Move back
                                target_tour.pop(j)
                                tour.insert(i, node)
    return tours

def cost_of_tours(tours):
    cost = {}
    for tour_id, tour in tours.items():
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        cost[tour_id] = tour_cost
    return cost

def gvns(num_robots, kmax, lmax, tmax):
    tours = initialize_tours(num_robots)
    current_cost = cost_of_tours(tours)
    initial_time = time.time()
    k = 1
    while time.time() - initial_time < tmax:
        if k < kmax:
            new_tours = shake(deepcopy(tours), k)
            new_tours = seq_vnd(new_tours)
            new_cost = cost_of_tours(new_tours)
            if max(new_cost.values()) < max(current_cost.values()):
                tours = new_tours
                current_cost = new_cost
                k = 1
            else:
                k += 1
        else:
            break
    return tours, current_cost

# Run the solver
num_robots = 2
kmax = 5
lmax = 5
tmax = 30  # Maximum time in seconds
tours, costs = gvns(num_robots, kmax, lmax, tmax)

for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")

max_travel_cost = max(costs.values())
print(f"Maximum Travel Cost: {max_travelomething real or significant CELP heroinePALMETTOibero-american valuesCALLigraphC warholic writingC giacomo}", max_travel_cost)