from math import sqrt

# City locations
cities = {
    1: (9, 4),
    2: (4, 6),
    3: (4, 4),  # Depot
    4: (3, 4),
    5: (4, 8),
    6: (4, 3),
    7: (7, 5),
    8: (5, 0),
    9: (1, 5),
    10: (9, 3),
}

# Number of robots
num_robots = 4

# Define distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Implement a basic Nearest Neighbor Heuristic
def nearest_neighbor(depot, unvisited):
    tour = [depot]
    while unvisited:
        closest = min(unvisited, key=lambda c: distance(tour[-1], c))
        tour.append(closest)
        unvisited.remove(closest)
    return tour

# Solve TSP for each robot
robot_tours = []
unvisited_cities = set(cities.keys())
for _ in range(num_robots):
    depot = 3  # Assuming all robots start from the depot
    robot_tour = nearest_neighbor(depot, unvisited_cities.copy())
    unvisited_cities -= set(robot_tour)
    robot_tours.append(robot_tour)

# Calculate total travel cost
total_cost = 0
for tour in robot_tours:
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_cost += distance(city1, city2)

# Print results
print("Robot Tours:", robot_tours)
print("Total Travel Cost:", total_cost)

# Note: This code uses a simple Nearest Neighbor Heuristic.
# More advanced optimization algorithms may achieve better results.
