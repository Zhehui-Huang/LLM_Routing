import math

# City coordinates with (x, y) tuples
city_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 27), (37, 69), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

num_robots = 2
depot_index = 0

# Function to calculate Euclidean distance between two cities indices
def distance(i, j):
    x1, y1 = city_coordinates[i]
    x2, y2 = city_storage[j]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to generate an initial solution using the nearest neighbor algorithm
def nearest_neighbor(start_index, cities):
    tour = [start_index]
    unvisited = set(cities)
    undivisited.remove(start_index)
    
    current_index = start_index
    while unvisited:
        next_index = min(unvisited, key=lambda index: distance(current_index, index))
        tour.append(next_index)
        current_index = next_index
        unvisited.remove(next_index)
    tour.append(start_index)  # return to depot
    return tour

# Function to perform 2-opt optimization on a given tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i], tour[j]) + distance(tour[i + 1], tour[j + 1]) < distance(tour[i], tour[i + 1]) + distance(tour[j], tour[j + 1]):
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    return tour

# Calculation of the tour cost
def calc_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign cities to each robot
cities_per_robot = len(city_coordinates[1:]) // num_robots
robot_tours = []
for r in range(num_robots):
    if r < num_robots - 1:
        cities = list(range(1 + r * cities_per_robot, (r + 1) * cities_per_robot))
    else:  # Last robot takes any unassigned cities
        cities = list(range(1 + r * cities_per_robot, len(city_coordinates)))
    initial_tour = nearest_neighbor(0, cities)
    optimized_tour = two_opt(initial_tour)
    robot_tours.append(optimized_tour)

# Display the tour and costs for each robot
overall_cost = 0
for idx, tour in enumerate(robot_tours):
    tour_cost = calc_tour_cost(tour)
    overall_cost += tour_cost
    print(f'Robot {idx} Tour: {tour}')
    print(f'Robot {idx} Total Travel Cost: {tour_cost:.2f}')

# Display the overall cost
print(f'Overall Total Travel Cost: {overall_cost:.2f}')