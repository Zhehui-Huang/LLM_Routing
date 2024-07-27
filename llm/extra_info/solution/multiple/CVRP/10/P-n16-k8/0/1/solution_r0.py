import math
from itertools import permutations

# Helper function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number and capacity of robots
num_robots = 8
capacity = 35

# Compute the pairwise city distances
num_cities = len(coordinates)
distances = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calc_distance(coordinates[i], coordinates[j])

# Determine the tours (This should ideally be solved using a sophisticated VRP solver,
# here we employ a simpler heuristic approach due to the complexity constraint.)

# A simple heuristic: nearest neighbor approach that respects vehicle capacity
def find_tours():
    remaining_demand = demands[:]
    tours = []
    for _ in range(num_robots):
        current_city = 0
        load = 0
        tour = [0]
        while True:
            # Find the nearest city that has unserved demand and can fit in the remaining capacity
            next_city = None
            min_distance = float('inf')
            for i in range(1, num_cities):
                if remaining_demand[i] > 0 and load + remaining_demand[i] <= capacity and distances[current_city][i] < min_distance:
                    next_city = i
                    min_distance = distances[current_city][i]
            if next_city is None:
                break
            tour.append(next_city)
            load += remaining_demand[next_city]
            remaining_demand[next_city] = 0
            current_city = next_city
        tour.append(0)  # Return to depot
        tours.append(tour)
        if all(d == 0 for d in remaining_demand):
            break
    return tours

# Calculate and output the results
def calculate_total_cost(tours):
    total_cost = 0
    for i, tour in enumerate(tours):
        cost = sum(distances[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")
        total_cost += cost
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

tours = find_tours()
calculate_total_tours_cost = calculate_total_cost(tours)