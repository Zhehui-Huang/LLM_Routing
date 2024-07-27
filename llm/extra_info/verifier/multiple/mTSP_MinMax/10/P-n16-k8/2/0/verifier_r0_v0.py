import math

# Coordinates of cities indexed from 0 through 15
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities (given their index) """
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Robots' tours given in the solution
robot_tours = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 0], [0, 9, 0], [0, 0], [0, 10, 0], [0, 0], 
    [0, 11, 0], [0, 0], [0, 12, 0], [0, 0], [0, 13, 0], [0, 0], [0, 14, 0], [0, 0], [0, 15, 0]
]

# Individual costs and a list to track all cities visited by robots
total_costs = []
all_visited_cities = set()

# Calculate travel cost for each tour and collect visited cities
for tour in robot_tours:
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
        all_visited_cities.add(tour[i])
    total_costs.append(cost)
    all_visited_cities.add(tour[-1])  # Add the last city of each tour

# Checking if all cities, except depot, are visited at least once
all_cities = set(range(1, 16))  # Cities 1 through 15 need to be visited
visited_cities = all_visited_cities.difference({0})
cities_visited_once = visited_cities == all_cities

# Calculate maximum travel cost
max_travel_cost = max(total_costs)

# Conditions to output "CORRECT" or "FAIL"
results = []
results.append(all(city[0] == 0 and city[-1] == 0 for city in robot_tours))  # All tours start and end at depot
results.append(cities_visited_once)  # All cities are visited at least once exactly (except depot)
results.append(max_travel_cost == 171)  # True if reported max travel cost matches the max cost from calculation

if all(results):
    print("CORRECT")
else:
{
    print("FAIL")
}