import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate the distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # infinity cost to travel to itself

# Each robot starts and ends at its own depot
robots = list(range(8))

def find_min_tour(robot):
    start = robot
    other_cities = [i for i in cities if i != start]
    min_cost = float('inf')
    best_tour = None

    for tour in permutations(other_cities):
        cost = distance_matrix[start][tour[0]] + sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + distance_matrix[tour[-1]][start]
        if cost < min_cost:
            min_cost = cost
            best_tour = [start] + list(tour) + [start]
            
    return best_tour, min_cost

overall_total_cost = 0
for robot in robots:
    tour, cost = find_min_tour(robot)
    overall_total_output_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")