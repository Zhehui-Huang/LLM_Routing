import math
from typing import List, Tuple

# City coordinates (index 0 is depot)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Euclidean distance calculator
def distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initial allocations of tours, assuming 8 robots
num_robots = 8
tours = [[0] for _ in range(num_robots)]  # start each tour from the depot

# Assign cities to robots in a round-robin manner (naive approach)
city_assigned = [False] * len(cities)  # to keep track of assigned cities
city_assigned[0] = True  # Depot city is not a destination

for i in range(1, len(cities)):
    min_index = i % num_robots
    tours[min_index].append(i)
    city_assigned[i] = True

# Return to depot to complete each tour
for tour in tours:
    tour.append(0)

# Calculate cost for each robot's tour
def calculate_tour_cost(tour: List[int]) -> float:
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Display the results
overall_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour)
    overall_cost += tour_cost
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {round(tour_cost, 2)}')

print(f'Overall Total Travel Cost: {round(overall_cost, 2)}')