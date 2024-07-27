import numpy as np

# City coordinates and number of robots
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], 
    [42, 41], [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], 
    [43, 67], [58, 48], [58, 27], [37, 69], [38, 46], [61, 33], 
    [62, 63], [63, 69], [45, 35], [32, 39], [56, 37]
])
num_robots = 8

# Calculate the Euclidean distance between two cities
def euclidean_dist(city1, city2):
    return np.linalg.norm(coordinates[city1] - coordinates[city2])

# Assign cities to robots; this implementation groups cities simply in successive blocks
def assign_cities_to_robots(coordinates, num_robots):
    num_cities = len(coordinates) - 1  # minus the depot
    cities_per_robot = num_cities // num_robots
    assignments = []
    for i in range(num_robots):
        if i < num_robots - 1:
            portion = list(range(1 + i * cities_per_robot, 1 + (i + 1) * cities_per_robot))
        else:
            portion = list(range(1 + i * cities_per_robot, num_cities + 1))
        assignments.append([0] + portion + [0])
    return assignments

# Nearest neighbor tour construction
def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_dist(current, x))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(0)
    return tour

# Calculate total travel cost
def calculate_travel_cost(tour):
    return sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign cities to robots using simple sequential assignment
robot_assignments = assign_cities_to_robots(coordinates, num_robots)

# Calculate tours and costs for each robot
tours = []
costs = []

for assignment in robot_assignments:
    cities = assignment[1:-1]
    tour = nearest_neighbor_tour(0, cities.copy())
    cost = calculate_travel_cost(tour)
    tours.append(tour)
    costs.append(cost)

# Output results
overall_total_cost = sum(costs)

for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")