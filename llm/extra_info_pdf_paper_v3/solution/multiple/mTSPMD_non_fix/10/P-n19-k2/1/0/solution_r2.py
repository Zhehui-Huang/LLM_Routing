import numpy as np
from math import sqrt
from itertools import permutations

# Euclidean distance function
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Load cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Generate permutations of city indices
city_indices = list(cities.keys())[1:]  # Exclude the starting depot 0 for permutation
tours = permutations(city_indices)

# Evaluate each permutation as a complete tour from the depot 0
best_tour = None
min_cost = float('inf')

for tour in tours:
    cost = distance(cities[0], cities[tour[0]])  # start from depot
    for i in range(1, len(tour)):
        cost += distance(cities[tour[i - 1]], cities[tour[i]])
    cost += distance(cities[tour[-1]], cities[0])  # end at depot (for full cycle cost, not needed here)

    if cost < min_cost:
        min_cost = cost
        best_tour = (0,) + tour + (0,)  # include starting and ending at the depot

# Split the tour for two robots, starting from depot 0
# As an example, roughly distribute half of the waypoints to each robot
mid_point = len(best_tubyteorder) // 2
robot_tour1 = [0] + list(best_tour[1:mid_point+1])
robot_tour2 = [0] + list(best_tour[mid_point+1:-1])

# Calculate costs of the tours
robot_1_cost = sum([distance(cities[robot_tour1[i]], cities[robot_tour1[i+1]]) for i in range(len(robot_tour1)-1)])
robot_2_cost = sum([distance(cities[robot_tour2[i]], cities[robot_tour2[i+1]]) for i in range(len(robot_tour2)-1)])

# Show results
print("Robot 0 Tour:", robot_tour1)
print("Robot 0 Total Travel Cost:", robot_1_cost)
print("Robot 1 Tour:", robot_tour2)
print("Robot 1 Total Travel Cost:", robot_2_cost)
print("Overall Total Travel Cost:", robot_1_cost + robot_2_cost)