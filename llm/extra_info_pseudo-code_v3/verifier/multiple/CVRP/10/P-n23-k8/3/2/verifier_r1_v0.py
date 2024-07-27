import numpy as np

# Provided city coordinates and demand
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46),
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8,
    11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15,
    21: 5, 22: 10
}

# Configuration
robot_capacity = 40
number_of_robots = 8

# Tours and total travel costs by robots as provided in the solution
robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]
robot_travel_costs = [72.09, 101.15, 61.09, 104.90, 95.16, 78.20, 106.50, 63.56]
computed_travel_costs = []

# Calculate Euclidean distance function
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Check if demand is fully met
city_demands_met = {i: 0 for i in demands}
for tour in robot_tours:
    for i in range(1, len(tour) - 1):
        city_demands_met[tour[i]] += demands[tour[i]]

demand_fulfilled = all(city_demands_met[city] == demands[city] for city in demands if city != 0)

# Check capacity constraints and compute travel costs for validation
capacity_constraints_met = True

for tour, reported_cost in zip(robot_tours, robot_travel_costs):
    load = 0
    travel_cost = 0
    for i in range(len(tour) - 1):
        load += demands[tour[i+1]]
        travel_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    computed_travel_costs.append(travel_cost)
    if load > robot_capacity:
        capacity_constraints_met = False
        break

# Ensure all tours start and end at the depot city 0
tours_correctly_formatted = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours)

# Verify the solution is using the exact number of specified robots
correct_number_of_robots = len(robot_tours) <= number_of_robots

# Validating reported costs somewhat closely match computed costs within rounding errors
valid_costs = all(abs(reported - computed) < 1 for reported, computed in zip(robot_travel_costs, computed_travel_costs))

# Check all requirements
if all([demand_fulfilled, capacity_constraints_met, tours_correctly_formatted, correct_number_of_robots, valid_costs]):
    print("CORRECT")
else:
    print("FAIL")