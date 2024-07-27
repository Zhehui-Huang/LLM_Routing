import math
import random
from heapq import nsmallest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
num_robots = 8

def initialize_tours(d, robots):
    distances = [(euclidean_distance(d[0], city), idx + 1) for idx, city in enumerate(d[1:])]
    sorted_distances = [item[1] for item in sorted(distances, key=lambda x: x[0])]
    tours = {i: [0] for i in range(robots)}
    assigned = []

    for i, city in enumerate(sorted_distances[:robots]):
        tours[i].extend([city, 0])
        assigned.append(city)

    unassigned = set(sorted_distances) - set(assigned)
    for city in unassigned:
        best_tour, min_increased_cost = min(
            ((robot, euclidean_distance(d[tours[robot][-2]], d[city-1]) 
                        - euclidean_distance(d[tours[robot][-2]], d[0])
                        + euclidean_distance(d[city-1], d[0]))
             for robot in range(robots)),
            key=lambda x: x[1]
        )
        tours[best_tour].insert(-1, city)

    return tours

def compute_tour_cost(tour, d):
    return sum(euclidean_distance(d[tour[i]], d[tour[i+1]]) for i in range(len(tour)-1))

def shaking(tours, d, k, robots):
    while k > 0:
        v = random.randint(0, robots - 1)
        if len(tours[v]) > 3:
            i = random.randint(1, len(tours[v]) - 3)
            city = tours[v].pop(i)
            t = random.choice([x for x in range(robots) if x != v])
            new_pos = random.randint(1, len(tours[t]) - 1)
            tours[t].insert(new_pos, city)
            k -= 1
    return tours

def perform_gvns(d, robots, k_max, t_max, l_max):
    current_tours = initialize_tours(d, robots)
    t = 0
    while t < t_max:
        k = 1
        while k < k_max:
            new_tours = shaking(current_tours.copy(), d, k, robots)
            # Normally Seq-VND would be called here
            new_costs = {robot: compute_tour_cost(tour, d) for robot, tour in new_tours.items()}
            max_new_cost = max(new_costs.values())

            old_costs = {robot: compute_tour_cost(tour, d) for robot, tour in current_tours.items()}
            max_old_cost = max(old_costs.values())

            if max_new_cost < max_old_cost:
                current_tours = new_tours
                k = 1
            else:
                k += 1
        t += 1
    return current_tours

final_tours = perform_gvns(cities, num_robots, k_max=5, t_max=10, l_max=5)
tour_costs = {robot: compute_tour_cost(tour, cities) for robot, tour in final_tours.items()}
max_cost = max(tour_costs.values())

for robot, tour in final_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")

print(f"Maximum Travel Cost: {max_cost}")