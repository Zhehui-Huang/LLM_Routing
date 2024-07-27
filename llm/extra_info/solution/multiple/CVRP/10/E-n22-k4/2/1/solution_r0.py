from itertools import permutations
from math import sqrt
import sys

# Define cities and coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Define demands for each city
demands = {
    0: 0,
    1: 1100,
    2: 700,
    3: 800,
    4: 1400,
    5: 2100,
    6: 400,
    7: 800,
    8: 100,
    9: 500,
    10: 600,
    11: 1200,
    12: 1300,
    13: 1300,
    14: 300,
    15: 900,
    16: 2100,
    17: 1000,
    18: 900,
    19: 2500,
    20: 1800,
    21: 700
}

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Begin solution (Greedy + Nearest Neighbour Strategy)
def solve():
    # Set of all cities excluding the depot
    cities_to_visit = set(cities.keys()) - {0}
    # Robots' tours initialized with starting city
    tours = {r: [0] for r in range(num_robots)}
    # Current robot load
    robot_loads = {r: 0 for r in range(num_robots)}
    # Tracking assigned demands
    demands_met = {city: False for city in cities if city != 0}
    current_city = {r: 0 for r in range(num_robots)}  # Robots start at city 0
    robot_position = 0
    total_travel_cost = 0

    while not all(demands_met.values()):
        # Assign cities to robots based on the nearest city that fits the remaining capacity
        for robot in range(num_robots):
            min_distance = float('inf')
            next_city = None
            for city in cities_to_visit:
                if not demands_met[city] and robot_loads[robot] + demands[city] <= robot_capacity:
                    distance = calculate_distance(current_city[robot], city)
                    if distance < min_distance:
                        min_distance = distance
                        next_city = city

            if next_city is not None:
                # Update tour and capacities
                tours[robot].append(next_city)
                robot_loads[robot] += demands[next_city]
                demands_met[next_city] = True
                total_travel_cost += min_distance
                current_city[robot] = next_city
                cities_to_visit.remove(next_city)

    # Return robots to depot
    for robot in range(num_robots):
        tours[robot].append(0)
        total_travel_rate = calculate_distance(current_city[robot], 0)
        total_travel_cost += total_travel_rate

    # Output results
    for robot in range(num_robots):
        tour_cost = sum(calculate_distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
        print(f"Robot {robot} Tour: {tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_travel(sub_total_costs):.2f}")

solve()