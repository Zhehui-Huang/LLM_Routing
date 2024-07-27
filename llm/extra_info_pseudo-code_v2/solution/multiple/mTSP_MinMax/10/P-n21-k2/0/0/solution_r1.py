import math
import random

# Distance Function
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Initiate a basic solution where every robot takes an equal number of cities
def simple_initialization(coordinates, num_robots):
    n = len(coordinates)
    tours = {i: [0] for i in range(num_robots)}
    cities_per_robot = (n - 1) // num_robots
    
    # Assign cities sequentially
    cities = list(range(1, n))
    for i, city in enumerate(cities):
        tours[i % num_robots].append(city)

    for tour in tours.values():
        tour.append(0) # return to depot

    return tours

# Calculate the tour distance
def calculate_tour_distance(tour, coordinates):
    return sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Define the problem
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

NUM_ROBOTS = 2

# Initialization
tours = simple_initialization(coordinates, NUM_ROBOTS)

# Calculate and print results
max_travel_cost = 0
for i in range(NUM_ROBOTS):
    tour_cost = calculate_tour_distance(tours[i], coordinates)
    if tour_cost > max_travel_cost:
        max_travel_cost = tour_cost
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")