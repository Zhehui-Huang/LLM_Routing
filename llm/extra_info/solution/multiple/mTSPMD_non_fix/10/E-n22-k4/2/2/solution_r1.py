import math
from heapq import heappop, heappush

# Calculating Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generating distance matrix
def generate_distance_matrix(coords):
    num_cities = len(coords)
    return [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Simple greedy algorithm for TSP, adapted for VRP across multiple robots
def simple_greedy_vrp(num_robots, depot, distance_matrix):
    num_cities = len(distance_matrix)
    visited = set()
    tours = [[] for _ in range(num_robots)]
    costs = [0] * num_robots
    city_heap = []

    # Initialize each robot at the depot city
    for i in range(num_robots):
        heappush(city_heap, (0, depot, i))  # (current cost, current city, robot id)
        visited.add(depot)
        tours[i].append(depot)

    # Assign cities to each robot
    while len(visited) < num_cities:
        cost, current_city, robot_id = heappop(city_heap)

        # Find the nearest unvisited city
        min_cost = float('inf')
        next_city = None
        for city in range(num_cities):
            if city not in visited and current_city != city:
                new_cost = distance_matrix[current_city][city]
                if new_cost < min_cost:
                    min_cost = new_cost
                    next_city = city

        # Update the robot's tour
        if next_city is not None:
            tours[robot_id].append(next_city)
            costs[robot_id] += min_cost
            visited.add(next_city)
            heappush(city_heap, (costs[robot_id], next_city, robot_id))

    # Close the tours at the depot for easier calculation, not required to stop at depot
    overall_cost = 0
    for i in range(num_robots):
        if len(tours[i]) > 1:
            last_city = tours[i][-1]
            return_home_cost = distance_matrix[last_city][depot]
            costs[i] += return_home_cost
            tours[i].append(depot)
        overall_cost += costs[i]

    return tours, costs, overall_cost

# Environment data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

distance_matrix = generate_distance_matrix(coordinates)
tours, costs, overall_cost = simple_greedy_vrp(4, 0, distance_matrix)

for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")