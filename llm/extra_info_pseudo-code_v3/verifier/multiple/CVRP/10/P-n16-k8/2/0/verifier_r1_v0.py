import math
from collections import defaultdict

# Data from the problem statement
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]
city_demand = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35

# Solution provided
tours = [
    [0, 6, 0], [0, 1, 12, 0], [0, 10, 3, 9, 0], 
    [0, 2, 0], [0, 4, 15, 0], [0, 7, 13, 0], 
    [0, 5, 14, 0], [0, 11, 8, 0]
]
travel_costs = [24.08, 60.01, 89.24, 42.05, 61.08, 60.36, 62.44, 92.23]

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if all cities are visited exactly once and demand is met
visited_cities = defaultdict(int)
for tour in tours:
    for i in range(1, len(tour) - 1):
        visited_cities[tour[i]] += 1

# Check if demands are fully met and cities are correctly included
correct_demands_and_visits = all(visited_cities[i] == 1 for i in range(1, 16)) and sum(visited_cities.values()) == 15

# Check if tours are valid (start and end at the depot), and if capacities are not violated
valid_tours_and_capacities = True
total_calculated_cost = 0
for tour, reported_cost in zip(tours, travel_costs):
    if tour[0] != 0 or tour[-1] != 0:
        valid_tours_and_capacities = False
        break
    load = 0
    actual_cost = 0
    for i in range(len(tour) - 1):
        load += city_demand[tour[i + 1]]
        actual_cost += calculate_distance(tour[i], tour[i + 1])
    valid_tours_and_capacities &= load <= robot_capacity and abs(actual_cost - reported_cost) < 0.1
    total_calculated_cost += reported_cost

total_reported_cost = sum(travel_costs)
if correct_demands_and_visits and valid_tours_and_capacities and abs(total_calculated_cost - total_reported_cost) < 0.1:
    print("CORRECT")
else:
    print("FAIL")