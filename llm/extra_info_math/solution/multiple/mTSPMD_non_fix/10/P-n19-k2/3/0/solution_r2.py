import math
from itertools import permutations

# Coordinates of cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the minimum tour cost using a greedy approach
def minimal_tsp_greedy(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    tour_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour_cost += distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    return tour, tour_cost

# Split tours between two robots
def split_tours_greedy():
    full_tour, full_cost = minimal_tsp_greedy(0)  # start from city 0
    mid_point = len(full_tour) // 2

    # Assign each half to a robot
    robot0_tour = full_tour[:mid_point]
    robot1_tour = full_tour[mid_point:]

    robot0_cost = sum(distance(robot0_tour[i], robot0_tour[i+1]) for i in range(len(robot0_tour)-1))
    robot1_cost = sum(distance(robot1_tour[i], robot1_tour[i+1]) for i in range(len(robot1_tour)-1))

    return robot0_tour, robot0_cost, robot1_tour, robot1_cost

# Get the tours and costs
robot0_tour, robot0_cost, robot1_tour, robot1_cost = split_tours_greedy()

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("\nRobot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("\nOverall Total Travel Cost:", robot0_cost + robot1_cost)