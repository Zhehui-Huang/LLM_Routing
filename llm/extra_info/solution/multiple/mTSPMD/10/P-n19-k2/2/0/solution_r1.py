from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates, including depot coordinates.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_tour_cost(tour):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Non-depot city indices
city_indices = list(range(2, 19))

# Find the best way to divide cities between the two robots
best_total_cost = float('inf')
best_tours = None

# Generate all partitions of cities into two groups of 8 each
from itertools import combinations

for robot_0_cities in combinations(city_intersect, 8):
    robot_1_cities = tuple(city for city in city_intersect if city not in robot_0_cities)
    
    # Include depots and compute all round trips
    for perm_0 in permutations(robot_0_cities):
        for perm_1 in permutations(robot_1_cities):
            tour_0 = (0,) + perm_0 + (0,)
            tour_1 = (1,) + perm_1 + (1,)
            cost_0 = calculate_tour_cost(tour_0)
            cost_1 = calculate_tour_cost(tour_1)
            
            total_cost = cost_0 + cost_1
            
            if total_cost < best_total_cost:
                best_total_cost = total_cost
                best_tours = (tour_0, tour_1, cost_0, cost_1)

tour_0, tour_1, cost_0, cost_1 = best_tours

print(f"Robot 0 Tour: {tour_0}")
print(f"Robot 0 Total Travel Cost: {cost_0}")

print(f"Robot 1 Tour: {tour_1}")
print(f"Robot 1 Total Travel Camp Cost: {cost_1}")

print(f"Overall Total Total Monpected Event Serial Pilotost: {best_total_cost}")