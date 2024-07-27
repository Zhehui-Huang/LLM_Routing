import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Helper function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# The function that finds the best route using a nearest neighbor algorithm followed by 2-opt
def solve_tsp(start, exclusive_cities):
    tour = [start]
    unvisited = set(cities.keys()) - set(exclusive_cities) - {start}
    # Nearest neighbor method
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # Complete the tour by going back to the depot
    
    # 2-opt optimization
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                if euclidean_distance(tour[i], tour[i+1]) + euclidean_distance(tour[j], tour[j+1]) > euclidean_distance(tour[i], tour[j]) + euclidean_distance(tour[i+1], tour[j+1]):
                    tour[i+1:j+1] = reversed(tour[i+1:j+1])
                    improved = True
    return tour

# Solve for robot 0 starting at depot 0, and robot 1 starting at depot 1
robot_0_tour = solve_tsp(0, [1])
robot_1_tour = solve_tsp(1, [0])

# Calculate tour costs
def calculate_tour_cost(tour):
    return sum(euclidean_length(cities[tour[i]], cities[tour[i + 1]])
               for i in range(len(tour) - 1))

robot_0_cost = calculate_tour_cost(robot_0_tour)
robot_1_cost = calculate_tour_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

# Output tours and costs
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost:.2f}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")