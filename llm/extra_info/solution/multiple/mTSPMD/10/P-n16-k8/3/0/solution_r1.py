import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities mapped by their indices
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robots and their start and end depots
robots_info = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

def compute_distance(p1, p2):
    """Compute Euclidean distance between two points."""
    return euclidean(p1, p2)

def total_trip_cost(tour):
    """Calculate the return distance trip cost for a given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += compute_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

def create_initial_tour(depots, cities):
    """Create an initial greedy tour based on nearest neighbour heuristic from depots."""
    tours = {}
    overall_cost = 0

    for robot_id, depot in depots.items():
        tour = [depot]
        remaining_cities = set(cities) - set(tour)

        while remaining_cities:
            last_city = tour[-1]
            next_city = min(remaining_cities, key=lambda x: compute_distance(coordinates[last_city], coordinates[x]))
            tour.append(next_city)
            remaining_cities.remove(next_city)
        
        tour.append(depot)  # return to the start depot
        tours[robot_id] = tour
        tour_cost = total_trip_cost(tour)
        overall_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    
    print(f"Overall Total Travel Cost: {overall_cost}")
    return tours, overall_cost

# Assign robots to certain cities based on simple strategy (could be improved with optimization techniques like k-means for clustering)
robust_assignments = {}
all_cities = list(range(16))  # list of all city indices

# Initially distribute non-depot cities among robots
free_cities = sorted(set(all_cities) - set(robots_info.values()))
while free_cities:
    for r in robots_info:
        if not free_cities:
            break
        if r not in robust_assignments:
            robust_assignments[r] = []
        robust_assignments[r].append(free_cities.pop(0))

# Ensuring that each robot starts and ends at its depot
for r in robust_assignments:
    robust_assignments[r] = [robots_info[r]] + robust_assignments[r] + [robots_info[r]]

# Execute the tour computation
create_initial_tour(robots_info, all_cities)