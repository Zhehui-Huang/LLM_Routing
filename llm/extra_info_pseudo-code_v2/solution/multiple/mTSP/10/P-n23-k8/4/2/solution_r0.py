import numpy as np

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
    return np.linalg.norm(city1 - city2)

# Distribute cities to robots using a heuristic
def assign_cities_to_robots(coordinates, num_robots):
    num_cities = len(coordinates) - 1  # excluding the depot
    cities_per_robot = num_cities // num_robots
    assignments = []
    for i in range(num_robots):
        if i < num_robots - 1:
            cities_list = list(range(1 + i * cities_per_robot, 1 + (i + 1) * cities_per_robot))
        else:
            cities_list = list(range(1 + i * cities_per_robot, num_cities + 1))
        assignments.append([0] + cities_list + [0])  # each tour starts and ends at the depot (0)
    return assignments

# Initialize city assignments
robot_assignments = assign_cities_to_robots(coordinates, num_robots)

# Tour construction using nearest neighbor heuristic
def construct_tour(robot_assignment):
    tour = [0]  # start from the depot
    available_cities = robot_assignment[1:-1]  # the cities assigned to the robot excluding the depot repetitions
    current_city = 0
    while available_cities:
        next_city = min(available_cities, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        current_city = next_city
        available_cities.remove(next_city)
    tour.append(0)  # return to depot
    return tour

# Calculate the total travel cost for a tour
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_dist(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# All robots perform their tours
all_tours = [construct_tour(assignment) for assignment in robot_assignments]
all_costs = [calculate_travel_cost(tour) for tour in all_tours]
overall_cost = sum(all_costs)

# Output the results for each robot
for i, (tour, cost) in enumerate(zip(all_tours, all_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")