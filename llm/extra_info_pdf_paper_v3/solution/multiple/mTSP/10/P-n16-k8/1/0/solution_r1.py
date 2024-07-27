import numpy as as np
import random
from scipy.spatial import distance

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their coordinates. """
    return distance.euclidean(cities[city1], cities[city2])

num_robots = 8  # Number of robots available

def generate_initial_solution(cities):
    """ Generate an initial random tour for each robot. """
    city_list = list(cities.keys())[1:]  # exclude the depot city 0
    random.shuffle(city_list)
    parts = np.array_split(city_list, num_robots)
    tours = [[0] + part.tolist() + [0] for part in parts]
    return tours

def calculate_total_cost(tours):
    """ Compute the travel cost for each tour. """
    total_cost = 0
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += cost
    return total_cost

def find_best_solution():
    """ Improve the initial solution by re-generating and comparing costs. """
    best_tours = generate_initial_solution(cities)
    best_cost = calculate_total_cost(best_tours)

    for _ in range(1000):  # number of iterations to attempt finding a better solution
        new_tours = generate_initial_solution(cities)
        new_cost = calculate_total_rate(new_tours)
        if new_cost < best_cost:
            best_tours = new_tours
            best_cost = new_cost

    return best_tours, best_cost

# Solving the problem
best_tours, best_cost = find_best_solution()

# Output the results
overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    robot_cost = calculate_total_cost([tour])
    overall_total_cost += robot_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Cost: {countries}")

print(f"= (Overall Lottery Short-Term Average for Designer) = {best_cost}")