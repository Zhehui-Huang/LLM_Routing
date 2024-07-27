import math
import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

# Calculate distances between each pair of cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distance_matrix = [
    [distance(i, j) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Function to find routes for each robot
def find_routes():
    # Initial assignment of cities to robots using a greedy capacity and proximity based method
    cities = list(range(1, len(coordinates)))  # Excluding depot
    np.random.shuffle(cities)  # Randomization for variation in initial setup
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots

    for city in cities:
        # Assign city to a robot with enough remaining capacity and minimum additional distance
        best_robot = None
        min_additional_cost = float('inf')
        
        for robot in range(num_robots):
            if loads[robot] + demands[city] <= capacity:
                additional_cost = distance_matrix[0][city] if not tours[robot] else distance_matrix[tours[robot][-1]][city]
                if additional_cost < min_additional_cost:
                    min_additional_cost = additional_cost
                    best_robot = robot
        
        if best_robot is not None:
            tours[best_robot].append(city)
            loads[best_robot] += demands[city]

    # Ensure each tour starts and ends at the depot
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)

    return tours

tours = find_routes()

# Calculate total travel cost for each tour
def calculate_tour_costs(tours):
    total_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i + 1]]
        total_costs.append(tour_cost)
    return total_costs

tour_costs = calculate_tour_costs(tours)
overall_total_cost = sum(tour_costs)

# Output the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")