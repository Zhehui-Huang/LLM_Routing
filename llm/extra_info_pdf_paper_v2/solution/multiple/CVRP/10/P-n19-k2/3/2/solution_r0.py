import math
from itertools import permutations

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_route_cost(route, city_coordinates):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += compute_distance(city_coordinates[route[i]], city_coordinates[route[i+1]])
    return total_cost

def can_add_to_route(route, new_city, demands, capacity):
    current_load = sum(demands[i] for i in route)
    return (current_load + demands[new_city]) <= capacity

def find_best_tours(city_coordinates, demands, num_robots, robot_capacity):
    n = len(city_coordinates)
    all_cities = set(range(1, n))  # Exclude depot 0
    tours = [[] for _ in range(num_robots)]
    used_cities = set()

    while all_cities - used_cities:
        for r in range(num_robots):
            if not tours[r]:
                tours[r].append(0)  # Start with depot

            added = False
            for city in (all_cities - used_cities):
                if can_add_to_route(tours[r], city, demands, robot_capacity):
                    tours[r].append(city)
                    used_cities.add(city)
                    added = True
                    break
            
            if not added:  # no more cities can be added to this robot tour due to capacity constraints
                tours[r].append(0)  # return to depot
                if len(tours[r]) == 2:  # Only contains depot at start and end, remove route
                    tours[r] = []
                continue
        
        # If no cities were added in this round, break out to avoid infinite loop
        if all(len(set(tour) - {0}) for tour in tours) == len(used_cities):
            break

    # Ensure all tours end with the depot
    for tour in tours:
        if tour and tour[-1] != 0:
            tour.append(0)

    return tours

def main():
    city_coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    num_robots = 2
    robot_capacity = 160

    tours = find_best_tours(city_coordinates, demands, num_robots, robot_capacity)
    overall_total_cost = 0

    for idx, tour in enumerate(tours):
        cost = total_route_cost(tour, city_coordinates)
        overall_total_cost += cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")

main()