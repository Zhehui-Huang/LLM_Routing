import math
import random

# City coordinates with depot cities included
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Distance calculation utility
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initial solution based on nearest neighbor strategy
def nearest_neighbor_solution(depot, cities_left):
    tour = [depot]
    while cities_left:
        last = tour[-1]
        nearest = min(cities_left, key=lambda city: euclidean_distance(last, city))
        tour.append(nearest)
        cities_left.remove(nearest)
    return tour

# Generating initial tours for each robot
def generate_initial_tours():
    depots = [0, 0]  # Both robots start at depot city 0 as per problem information
    cities_left = set(cities.keys()) - {0}
    tours = []
    
    for depot in depots:
        tour = nearest_neighbor_solution(depot, cities_left)
        tours.append(tour)
        break  # Since all cities are picked in one go due to single depot in this strategy
    
    # If cities are still left, allocate to the 2nd robot
    if cities_left:
        tour = nearest_neighbor_solution(depots[1], cities_left)
        tours.append(tour)
    
    return tours

def total_tour_cost(tour):
    cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return cost

def print_solution(tours):
    total_cost = 0
    for idx, tour in enumerate(tours):
        cost = total_tour_cost(tour)
        total_cost += cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Costs: {total_cost:.2f}")

def main():
    tours = generate_initial_tours()
    print_solution(tours)

main()