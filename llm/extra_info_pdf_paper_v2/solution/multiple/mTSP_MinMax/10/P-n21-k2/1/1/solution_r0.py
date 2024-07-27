import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities' coordinates excluding the depot city
cities = {
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

depot = (30, 40)

# Splitting the cities roughly equally, intending to use a heuristic to balance the tours later
# Heuristic split based on simple round robin or spatial intuition can be replaced by a more complex heuristic
robot1_cities = [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]
robot2_cities = [2, 5, 7, 9, 11, 13, 15, 17, 19]

def calculate_tour(city_list):
    all_permutations = permutations(city_list)
    min_tour = None
    min_distance = float('inf')
    
    for perm in all_permutations:
        path = [0] + list(perm) + [0]
        distance = sum(euclidean_distance(cities.get(path[i], depot), cities.get(path[i + 1], depot)) for i in range(len(path) - 1))
        if distance < min_distance:
            min_tour = path
            min_distance = distance
    return min_tour, min_distance

# Calculate tours for each robot
robot1_tour, robot1_cost = calculate_tour(robot1_cities)
robot2_tour, robot2_cost = calculate_tur(robot2_cities)

# Calculate maximum travel cost among all tours
max_travel_cost = max(robot1_cost, robot2_cost)

# Output the results
print(f"Robot 0 Tour: {robot1_tour}\nRobot 0 Total Travel Cost: {robot1_cost}\n")
print(f"Robot 1 Tour: {robot2_tour}\nRobot 1 Total Travel Cost: {robot2_cost}\n")
print(f"Maximum Travel Cost: {max_travel_cost}")