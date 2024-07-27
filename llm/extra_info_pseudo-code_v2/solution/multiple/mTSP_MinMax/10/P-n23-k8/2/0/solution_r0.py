import math
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance calculation using Euclidean metric
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# The number of robots
num_robots = 8

# Initialization of tours
def initialize_tours():
    all_cities = list(cities.keys())[1:]  # Exclude the depot
    random.shuffle(all_cities)
    tours = [[] for _ in range(num_robots)]
    idx = 0
    for city in all_cities:
        tours[idx % num_robots].append(city)
        idx += 1
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

# Calculate the tour cost
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Perform one iteration of shaking
def shake(tours, k):
    for _ in range(k):
        # Choose two different tours randomly
        ta, tb = random.sample(tours, 2)
        if len(ta) > 2 and len(tb) > 2: # Ensure tours can be changed
            # Remove a random city from tour ta and insert into tb
            city = ta.pop(random.randint(1, len(ta) - 2))
            insert_idx = random.randint(1, len(tb) - 1)
            tb.insert(insert_idx, city)
    return tours

# Perform local search optimization (2-opt like)
def local_search(tours):
    improved = True
    while improved:
        improved = False
        for tour in tours:
            best_reduction = 0
            best_move = None
            for i in range(1, len(tour)-2):
                for j in range(i+2, len(tour)-1):
                    if i == 1 and j == len(tour) - 2:
                        continue
                    # Calculate the change in cost if we performed 2-opt here
                    current_distance = distance(tour[i], tour[i+1]) + distance(tour[j], tour[j+1])
                    new_distance = distance(tour[i], tour[j]) + distance(tour[i+1], tour[j+1])
                    reduction = current_distance - new_distance
                    if reduction > best_reduction:
                        best_reduction = reduction
                        best_move = (i, j)
            if best_move:
                i, j = best_move
                tour[i+1:j+1] = reversed(tour[i+1:j+1])
                improved = True
    return tours

def gvns(max_iterations=10000, shaking_strength=5):
    tours = initialize_tours()
    best_tours = tours[:]
    best_cost = max(calculate_tour_cost(tour) for tour in tours)
    iteration = 0

    while iteration < max_iterations:
        tours = shake(tours, shaking_strength)
        tours = local_search(tours)
        max_cost = max(calculate_tour_cost(tour) for tour in tours)
        if max_cost < best_cost:
            best_cost = max_cost
            best_tours = [tour[:] for tour in tours]
        iteration += 1
    
    return best_tours

# Running the GVNS
best_tours = gvns()

# Output the tours and the costs
max_travel_cost = -1
for index, tour in enumerate(best_tours):
    tour_cost = calculate_tour_cost(tour)
    max_travel_cost = max(max_travel_cost, tour_cost)
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {max_travel_cost:.2f}")