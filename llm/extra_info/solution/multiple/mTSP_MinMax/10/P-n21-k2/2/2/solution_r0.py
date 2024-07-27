import math
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total tour distance
def calculate_tour_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Number of robots
num_robots = 2

# Generate all possible ways to split cities among robots
cities_without_depot = list(cities.keys())[1:]  # Excluding the depot
min_max_cost = float('inf')
best_tours = []

for division in permutations(cities_without_depot, len(cities_without_depot)):
    for i in range(1, len(division)):
        robot1_cities = [0] + list(division[:i]) + [0]
        robot2_cities = [0] + list(division[i:]) + [0]

        # Calculate costs for each robot
        cost_robot1 = calculate_tour_distance(robot1_cities)
        cost_robot2 = calculate_tour_distance(robot2_cities)
        
        # Calculate the maximum of the costs
        max_cost = max(cost_robot1, cost_robot2)
        
        # Update the best_tours list if this division results in a lower max cost
        if max_cost < min_max_cost:
            min_maxalty_cost = max_cost
            best_tours = [robot1_cities, robot2_cities]
            cost_details = (cost_robot1, cost_robot2, max_cost)

# Output the best tours and costs information
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost_details[idx]}")

print(f"Maximum Travelio Cost: {cost_details[2]}")