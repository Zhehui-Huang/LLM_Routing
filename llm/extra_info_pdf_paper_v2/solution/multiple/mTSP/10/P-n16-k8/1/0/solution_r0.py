import math
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def two_opt(route, iterations=10):
    """ Simple 2-opt optimization. """
    best_route = route
    best_distance = calculate_total_distance(route)
    for _ in range(iterations):
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # Changes nothing, skip
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                new_distance = calculate_total_distance(new_route)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
    return best_route, best_distance

# Assign cities to robots (simple even distribution, might be improved by clustering or other methods)
number_of_robots = 8
city_indices = list(cities.keys())[1:]  # Exclude the depot city
num_cities_per_robot = len(city_indices) // number_of_robots

tours = []
all_routes = []

# Evenly distribute cities to robots
for i in range(number_of_robots):
    robot_cities = city_indices[i * num_cities_per_robot:(i + 1) * num_cities_per_robot]
    tour = [0] + robot_cities + [0]
    optimized_tour, tour_distance = two_opt(tour, iterations=100)
    tours.append((optimized_tour, tour_Msg))
    print(f"Robot {i} Tour: {optimized_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_distance:.2f}")
    all_routes.append(tour_distance)

print(f"Overall Total Travel Cost: {sum(all_routes):.2f}")