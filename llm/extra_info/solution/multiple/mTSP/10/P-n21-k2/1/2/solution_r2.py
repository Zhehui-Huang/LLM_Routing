import math

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, coordinates):
    """ Calculate the total cost of a given tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def find_minimal_tour(cities, coordinates):
    """ Find the minimal tour using a simple greedy nearest neighbor heuristic. """
    if not cities:
        return [], 0

    tour = [0]  # start at the depot
    current_city = 0
    unvisited = set(cities)
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to depot
    return tour, total_tour_cost(tour, coordinates)

def assign_cities_to_robots(number_of_robots, number_of_cities):
    """ Assign cities to robots in a round-robin manner. """
    assignments = [[] for _ in range(number_of_robots)]
    for city in range(1, number_of_cities):  # start from 1 to skip the depot
        robot_index = (city - 1) % number_of_robots
        assignments[robot_index].append(city)
    return assignments

# Robot and city configuration
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
num_robots = 2
num_cities = len(coordinates)  # total including depot

# Distribute cities among the robots
cities_for_robots = assign_cities_to_robots(num_robots, num_cities)

overall_total_cost = 0
results = []

# Compute tours for each robot
for idx, cities in enumerate(cities_for_robots):
    tour, cost = find_minimal_tour(cities, coordinates)
    overall_total_cost += cost
    results.append((idx, tour, cost))

# Print results
for robot_id, tour, cost in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")