import math

# Cities coordinates where the first element is the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Euclidean distance between two points
def distance(index1, index2):
    point1 = cities[index1]
    point2 = cities[index2]
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Number of robots
num_robots = 4
tours = {i: [0] for i in range(num_robots)}

# Simple greedy initialization of the tours
unvisited_cities = list(range(1, len(cities)))
assigned_cities = [False] * len(cities)

# Distribute cities among robots
robot = 0
while unvisited_cities:
    min_dist = float('inf')
    nearest_city = None
    current_city = tours[robot][-1]

    # Find the nearest unvisited city
    for city in unvisited_cities:
        dist = distance(current_city, city)
        if dist < min_dist:
            min_dist = dist
            nearest_city = city

    # Assign nearest city to current robot tour
    tours[robot].append(nearest_city)
    unvisited_cities.remove(nearest_city)

    # Move to next robot
    robot = (robot + 1) % num_robots

# Close the tours by returning to the depot
for i in range(num_robots):
    tours[i].append(0)

# Calculate the cost of each tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

tour_costs = {robot: calculate_tour_cost(tours[robot]) for robot in range(num_robots)}

# Find the maximum travel cost among all tours
max_cost = max(tour_costs.values())

# Output the solution
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")

print(f"Maximum Travel Cost: {max_cost}")