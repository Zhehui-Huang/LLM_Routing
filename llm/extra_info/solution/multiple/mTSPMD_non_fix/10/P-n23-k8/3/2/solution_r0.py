import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Here assuming there are 8 robots and all start at depot city 0
robots = 8
starting_depot = 0

def nearest_neighbor_tours(start_cities, all_cities):
    remaining = set(all_cities.keys()) - {start_cities}
    tours = []
    costs = []
    
    for start in start_cities:
        tour = [start]
        current = start
        cost = 0
        
        while remaining:
            next_city = min(remaining, key=lambda x: euclidean_distance(*all_cities[current], *all_cities[x]))
            cost += euclidean_distance(*all_cities[current], *all_cities[next_city])
            tour.append(next_city)
            current = next_city
            remaining.remove(next_city)
        
        tours.append(tour)
        costs.append(cost)
    
    return tours, costs

# For simplicity, first, let every robot start from depot 0 and get the nearest cities tours
tours, costs = nearest_neighbor_tours([0]*robots, cities)

# Calculate overall cost
overall_cost = sum(costs)

# Displaying the output in the required format
for i in range(len(tours)):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")