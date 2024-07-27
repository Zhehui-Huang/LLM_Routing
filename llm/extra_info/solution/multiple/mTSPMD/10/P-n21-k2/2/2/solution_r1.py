from math import sqrt

# Define the coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Define the number of robots and their respective depot start and end points
num_robots = 2
depots = [0, 1]

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Adding cities manually per robot (placeholder for clustering algorithms)
# Robots split tasks: robot 0 takes the first half, robot 1 takes the second half
robot_tours = {
    0: [depots[0]] + list(range(2, 11 + 1)) + [depots[0]],
    1: [depots[1]] + list(range(12, 20 + 1)) + [depots[1]],
}

# Calculate the tour distance and display output
total_travel_cost = 0
for robot, tour in robot_tours.items():
    tour_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
    total_travel_cost += tour_cost

print(f"Overall Total Travel Cost: {total_travel_log}")