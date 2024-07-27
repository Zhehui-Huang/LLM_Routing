import math
import random
from itertools import permutations

# Coordinates for the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def total_tour_cost(tour):
    """ Calculate the total travel cost of a tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

# Create initial assignments to each robot
cities = list(range(1, len(coordinates)))  # excluding the depot
random.shuffle(cities)
chunks = [cities[i::num_robots] for i in range(num_robots)]

# Generate the tours each robot will take, starting and ending at depot
tours = [[0] + chunk + [0] for chunk in chunks]

# Calculate tour costs and perform 2-opt optimization
def optimize_tour(tour):
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip consecutive cities (neighboring in tour)
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]  # reverse the segment between i and j
                if total_tour_cost(new_tour) < total_tour_cost(tour):
                    tour = new_tour
                    made_improvement = True
    return tour

optimized_tours = [optimize_tour(tour) for tour in tours]

# Calculate the cost of each optimized tour
tour_costs = [total_tour_cost(tour) for tour in optimized_tours]
overall_total_cost = sum(tour_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"\nOverall Total Travel Cost: {round(overall_total_cost, 2)}")