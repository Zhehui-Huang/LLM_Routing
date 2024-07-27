import numpy as np

# Function to split cities approximately equally
def split_cities(n, k):
    """ Split `n` cities into `k` approximately equal parts """
    avg = n / float(k)
    out = []
    last = 0.0

    while last < n:
        out.append(int(last + avg))
        last += avg
    return out

def create_tours(split, num_cities):
    tours = []
    start = 0
    for end in split:
        tours.append([0] + list(range(start+1, end+1)) + [0])
        start = end
    return tours

# Number of non-depot cities and number of robots
num_cities = len(cities) - 1  # minus the depot city
splits = split_cities(num_cities, num_robots)
tours = create_tours(splits, num_cities)

# Initialize best tours and minimum max cost found
best_tours = None
min_max_cost = float('inf')

# Check every permutation of cities within each half for better distribution
from itertools import permutations

# Compute each possible distribution of cities
for perm_tour1 in permutations(range(1, splits[0] + 1)):
    for perm_tour2 in permutations(range(splits[0] + 1, num_cities + 1)):
        current_tours = [
            [0] + list(perm_tour1) + [0],
            [0] + list(perm_tour2) + [0]
        ]

        # Calculate the costs for the current settings
        cost_robot1 = calculate_tour_distance(current_tours[0])
        cost_robot2 = calculate_tour_distance(current_tours[1])
        max_cost = max(cost_robot1, cost_robot2)

        # If a better max cost is found, store the result
        if max_cost < min_max_cost:
            min_max_cost = max_cost
            best_tours = current_tours
            cost_details = (cost_robot1, cost_robot2, max_cost)

# Output the best tours and costs information
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost_details[idx]}")

print(f"Maximum Travel Cost: {cost_details[2]}")