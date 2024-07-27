import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
depot = 0

# Prepare the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Initial naive split of cities to robots
cities_per_robot = len(cities) // num_robots
assignments = [list(range(1+robot*cities_per_robot, 1+(robot+1)*cities_per_robot)) for robot in range(num_robots)]
assignments[-1].extend(range(1+num_robots*cities_per_robot, len(cities)))  # Assign leftover cities to the last robot

def optimal_tour(cities_indices):
    best_route = None
    best_cost = float('inf')
    for perm in permutations(cities_indices):
        route = [depot] + list(perm) + [depot]
        cost = calculate_total_distance(route, distance_matrix)
        if cost < best_cost:
            best_cost = cost
            best_route = route
    return best_route, best_cost

tours = []
max_cost = 0

for robot, cities_indices in enumerate(assignments):
    tour, cost = optimal_tour(cities_indices)
    tours.append((tour, cost))
    max_cost = max(max_cost, cost)

# Output results
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")