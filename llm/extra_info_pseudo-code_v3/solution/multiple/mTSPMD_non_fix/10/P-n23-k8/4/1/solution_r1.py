import math
from collections import defaultdict

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Configuration
num_robots = 8
depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]

def initial_solution(depot_indices, num_robots):
    other_cities = set(cities.keys()) - set(depot_indices)
    tours = defaultdict(list)

    # Start each robot at a depot
    for i in range(num_robots):
        tours[i].append(depot_indices[i])

    # Assign nearest remaining city to the last city in each robot's tour until all cities are assigned
    while other_cities:
        for r in tours:
            last_city = tours[r][-1]
            nearest_city = None
            min_distance = float('inf')
            for city in other_cities:
                dist = euclidean_distance(cities[last_city], cities[city])
                if dist < min_distance:
                    min_distance = dist
                    nearest_city = city
            if nearest_city is not None:
                tours[r].append(nearest_city)
                other_cities.remove(nearest_city)

    # Calculate travel cost for each tour
    total_cost = 0
    for r in tours:
        tour_cost = 0
        tour = tours[r]
        for i in range(len(tour)-1):
            tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_depot_cost
        
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Generate and print the results of the initial solution
initial_solution(depot_indices, num_robots)