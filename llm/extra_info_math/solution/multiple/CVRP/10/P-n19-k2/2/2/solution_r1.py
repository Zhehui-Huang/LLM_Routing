import math
from collections import namedtuple

# Define the data using named tuples for better readability
City = namedtuple('City', ['index', 'demand', 'coordinates'])

# Data Initialization
cities = [
    City(0, 0, (30, 40)),
    City(1, 19, (37, 52)),
    City(2, 30, (49, 43)),
    City(3, 16, (52, 64)),
    City(4, 23, (31, 62)),
    City(5, 11, (52, 33)),
    City(6, 31, (42, 41)),
    City(7, 15, (52, 41)),
    City(8, 28, (57, 58)),
    City(9, 14, (62, 42)),
    City(10, 8, (42, 57)),
    City(11, 7, (27, 68)),
    City(12, 14, (43, 67)),
    City(13, 19, (58, 27)),
    City(14, 11, (37, 69)),
    City(15, 26, (61, 33)),
    City(16, 17, (62, 63)),
    City(17, 6, (63, 69)),
    City(18, 15, (45, 35))
]
capacity = 160
num_robots = 2

# Utility function to compute Euclidean distance
def distance(city1, city2):
    x1, y1 = city1.coordinates
    x2, y2 = city2.coordinates
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize tours
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
tours_costs = [0.0] * num_robots

# Assign cities to robots
for city in cities[1:]:  # Skip the depot city
    for robot in range(num_robots):
        if current_loads[robot] + city.demand <= capacity:
            if tours[robot]:
                last_city_index = tours[robot][-1]
                tours_costs[robot] += distance(cities[last_city_index], city)
            else:
                tours_costs[robot] += distance(cities[0], city)  # from depot to first city
            
            tours[robot].append(city.index)
            current_loads[robot] += city.demand
            
            break  # stop searching once the city is assigned

# Closing the tour back at the depot
for robot in range(num_robots):
    if tours[robot]:
        last_city_index = tours[robot][-1]
        tours_costs[robot] += distance(cities[last_city_index], cities[0])
        tours[robot].insert(0, 0)  # Start at depot
        tours[robot].append(0)  # Return to depot

# Output result
overall_total_cost = sum(tours_costs)
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tours_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")