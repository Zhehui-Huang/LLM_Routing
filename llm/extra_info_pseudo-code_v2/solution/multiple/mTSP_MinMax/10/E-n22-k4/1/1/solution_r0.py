import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def initialization(cities, num_robots):
    distances = [(i, euclidean_distance(cities[0], cities[i])) for i in range(1, len(cities))]
    distances.sort(key=lambda x: x[1])
    tours = {r: [0] for r in range(num_robots)}
    for index, (city_idx, _) in enumerate(distances):
        tours[index % num_robots].append(city_idx)
    for r in tours:
        tours[r].append(0)
    return tours

def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def perform_shaking(tours, cities, k):
    while k > 0:
        tour_keys = list(tours.keys())
        random_tour_key = random.choice(tour_keys)
        if len(tours[random_tour_key]) > 2:
            node_idx = random.choice(tours[random_tour_key][1:-1])
            tours[random_tour_key].remove(node_idx)
            target_tour_key = random.choice([t for t in tour_keys if t != random_tour_key])
            insert_pos = random.randint(1, len(tours[target_tour_key]) - 1)
            tours[target_tour_key].insert(insert_pos, node_idx)
            k -= 1
    return tours

def seq_vnd(tours, cities):
    improved = True
    while improved:
        improved = False
        for tour_key in list(tours.keys()):
            original_cost = calculate_tour_cost(tours[tour_key], cities)
            best_cost = original_cost
            for i in range(1, len(tours[tour_key]) - 2):
                for j in range(i + 1, len(tours[tour_key]) - 1):
                    tours[tour_key][i], tours[tour_key][j] = tours[tour_key][j], tours[tour_key][i]
                    current_cost = calculate_tour_cost(tours[tour_key], cities)
                    if current_cost < best_cost:
                        best_cost = current_cost
                        improved = True
                    else:
                        tours[tour_key][i], tours[tour_key][j] = tours[tour_key][j], tours[tour_key][i]
    return tours

def gvns(cities, num_robots, kmax, lmax, tmax):
    tours = initialization(cities, num_robots)
    t = 0
    while t < tmax:
        k = 1
        while k < kmax:
            new_tours = perform_shaking(tours, cities, k)
            better_tours = seq_vnd(new_tours, cities)
            new_cost = max(calculate_tour_cost(better_tours[r], cities) for r in better_tours)
            current_cost = max(calculate_tour_cost(tours[r], cities) for r in tours)
            if new_cost < current_cost:
                tours = better_tours
                k = 1
            else:
                k += 1
        t += 1
    
    max_cost = max(calculate_tour_cost(tours[r], cities) for r in tours)
    for r in tours:
        print(f"Robot {r} Tour: {tours[r]}")
        print(f"Robot {r} Total Travel Cost: {calculate_tour_cost(tours[r], cities)}")
    
    print(f"Maximum Travel Cost: {max_cost}")

# Define the cities coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), 
    (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), 
    (129, 189), (155, 185), (139, 182)
]

# Parameters
num_robots = 4
kmax = 5
lmax = 5
tmax = 5

# Solve using GVNS
gvns(cities, num_robots, kmax, lmax, tmax)