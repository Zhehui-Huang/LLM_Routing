import math
import random

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    return sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

def initialization(coordinates, num_robots):
    n = len(coordinates)
    nodes = list(range(1, n))  # exclude the depot which is 0
    random.shuffle(nodes)  # shuffle nodes to distribute them randomly
    tours = {i: [0] for i in range(num_robots)}  # start each tour at the depot

    for index, node in enumerate(nodes):
        min_tour = min(tours, key=lambda k: calculate_total_distance(tours[k] + [node, 0], coordinates))
        tours[min_tour].append(node)

    for k in tours:
        tours[k].append(0)  # end each tour at the depot
    
    return tours

def shake(tours, k, coordinates):
    for _ in range(k):
        chosen_tours = random.sample(tours.keys(), 2)
        if len(tours[chosen_tours[0]]) > 2 and len(tours[chosen_tours[1]]) > 2:  # ensure tours can exchange
            i = random.randint(1, len(tours[chosen_tours[0]]) - 2)
            node = tours[chosen_tours[0]][i]
            tours[chosen_tours[0]].remove(node)
            tours[chosen_tours[1]].insert(random.randint(1, len(tours[chosen_tours[1]]) - 1), node)
    return tours

def local_search(tour, coordinates):
    # 2-opt local search
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour)):
                if j - i == 1:
                    continue
                if distance(coordinates[tour[i-1]], coordinates[tour[j]]) +\
                   distance(coordinates[tour[i]], coordinates[tour[j+1]]) <\
                   distance(coordinates[tour[i-1]], coordinates[tour[i]]) +\
                   distance(coordinates[tour[j]], coordinates[tour[j+1]]):
                    tour[i:j] = tour[j:i-1:-1]
                    made_improvement = True
    return tour

def GVNS(coordinates, num_robots, kmax, tmax):
    tours = initialization(coordinates, num_robots)
    best_solution = tours
    best_max_distance = max(calculate_total_distance(tours[k], coordinates) for k in tours)
    t_start = time.time()
    
    while time.time() - t_start < tmax:
        k = 1
        while k < kmax:
            new_tours = shake(tours, k, coordinates)
            for key in new_tours:
                new_tours[key] = local_search(new_tours[key], coordinates)
            max_distance = max(calculate_total_distance(new_tours[k], coordinates) for k in new_tours)
            
            if max_distance < best_max_distance:
                best_solution, best_max_distance = new_tours, max_distance
                k = 1
            else:
                k += 1
    
    return best_solution

# Define the coordinates as provided
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

NUM_ROBOTS = 2
KMAX = 10
TMAX = 30  # Seconds

final_tours = GVNS(coordinates, NUM_ROBOTS, KMAX, TMAX)

for i, tour in final_tours.items():
    tour_cost = calculate_total_distance(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

max_tour_cost = max(calculate_total_distance(final_tours[i], coordinates) for i in final_tours)
print(f"Maximum Travel Cost: {max_tour_cost}")