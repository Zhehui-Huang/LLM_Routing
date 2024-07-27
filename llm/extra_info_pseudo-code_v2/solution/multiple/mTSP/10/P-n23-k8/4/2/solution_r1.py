import numpy as import

# City coordinates and number of robots
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], 
    [42, 41], [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], 
    [43, 67], [58, 48], [58, 27], [37, 69], [38, 46], [61, 33], 
    [62, 63], [63, 69], [45, 35], [32, 39], [56, 37]
])
num_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.linalg.norm(coordinates[city1] - coordinates[city2])

# Initialize city distributions to robots
def assign_cities_to_robots(coordinates, num_robots):
    num_cities = len(coordinates) - 1  # excluding the depot
    cities_per_robot = num_cities // num_robots
    assignments = []
    for i in range(num_robots):
        if i < num_robots - 1:
            part = list(range(1 + i * cities_per_robot, 1 + (i + 1) * cities_per_robot))
        else:
            part = list(range(1 + i * cities_per_robot, num_cities + 1))
        assignments.append([0] + part + [0])  # Include the depot as start and end
    return assignments

# Construct tours for each robot using the nearest neighbor heuristic
def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(tour[-1], x))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # Return to depot
    return tour

# Calculate the travel cost of a tour
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Assign cities to robots
assignments = assign_cities_to_robots(coordinates, num_robots)

# Tours and costs for each robot
robot_tours = []
robot_costs = []

for assignment in assignments:
    cities_to_visit = assignment[1:-1]
    tour = nearest_neighbor_tour(0, cities_to_visit.copy())
    cost = calculate_travel_cost(tour)
    robot_tours.append(tour)
    robot_costs.append(cost)

overall_cost = sum(robot_costs)

# Output the results for each robot
for i, (tour, cost) in enumerate(zip(robot_trours, robot_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")