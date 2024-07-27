import math
from itertools import combinations

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

def get_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

def savings_list():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            saving = get_distance(depot, i) + get_distance(depot, j) - get_distance(i, j)
            savings.append((saving, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def can_merge(tour1, tour2, demands, capacity):
    if tour1[0] != depot or tour1[-1] != depot or tour2[0] != depot or tour2[-1] != depot:
        return False
    total_demand = sum(demands[i] for i in tour1[1:-1] + tour2[1:-1])
    return total_demand <= capacity

def merge_tours(tours, savings):
    merged = True
    while merged:
        merged = False
        for saving, i, j in savings:
            tour_i = next((t for t in tours if i in t[1:-1]), None)
            tour_j = next((t for t in tours if j in t[1:-1]), None)
            if tour_i and tour_j and tour_i != tour_j:
                if can_merge(tour_i, tour_j, demands, robot_capacity):
                    tours.remove(tour_i)
                    tours.remove(tour_j)
                    new_tour = [depot] + tour_i[1:-1] + tour_j[1:-1] + [depot]
                    tours.append(new_tour)
                    merged = True
                    break
    return tours

def create_initial_tours(demands, capacity):
    tours = []
    for i in range(1, len(demands)):
        if demands[i] <= capacity:
            tours.append([depot, i, depot])
    return tours

def solve_cvrp():
    initial_tours = create_initial_tours(demands, robot_capacity)
    savings = savings_list()
    tours = merge_tours(initial_tours, savings)

    total_cost = 0
    for index, tour in enumerate(tours):
        tour_cost = sum(get_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

solve_cvrp()