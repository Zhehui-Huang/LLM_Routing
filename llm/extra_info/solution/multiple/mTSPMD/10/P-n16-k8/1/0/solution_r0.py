import math
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and their depot assignments
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial assignment of cities to each robot, robots can start with their respective depots
tours = {r: [depot] for r, depot in robots.items()}

# Assigning unique cities to robots tentatively based on the nearest depot policy
assigned_cities = set(robots.values())
for city in cities:
    if city not in assigned_cities:
        nearest_depot = min(robots, key=lambda depot: calculate_distance(city, robots[depot]))
        tours[nearest_depot].append(city)
        assigned_cities.add(city)

# Calculating the best route for each robot by permutation and minimum distance calculation
def find_best_route(robot_id, tour):
    depot = robots[robot_id]
    min_route = None
    min_cost = float('inf')
    cities_to_permute = tour[1:]  # Avoid including depot in permutations
    for perm in permutations(cities_to_permute):
        route = [depot] + list(perm) + [depot]
        cost = sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))
        if cost < min_cost:
            min_cost = cost
            min_route = route
    return min_route, min_cost

# Display results
overall_cost = 0
for robot in robots:
    best_tour, tour_cost = find_best_route(robot, tours[robot])
    print(f'Robot {robot} Tour: {best_tour}')
    print(f'Robot {robot} Total Travel Cost: {tour_cost}')
    overall_cost += tour_cost

print(f'Overall Total Travel Cost: {overall_cost}')