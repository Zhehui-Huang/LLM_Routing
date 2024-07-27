import numpy as np
from math import sqrt

# City data and parameters
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
}
n_cities = len(cities)
m = 2  # Number of robots

# Helper function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to initialize solutions
def initialize_solution():
    distances = np.array([euclidean_distance(cities[0], cities[i]) for i in range(1, n_cities)])
    order = np.argsort(distances)
    tours = [[] for _ in range(m)]
    for i in range(m):
        tours[i].append(order[i] + 1)  # Adding 1 to account for 0-indexing in python

    for i in range(m, n_cities - 1):
        min_additional_cost = float('inf')
        min_tour = None
        
        for tour in tours:
            current_cost = sum([euclidean_distance(cities[tour[j]], cities[tour[j + 1]]) for j in range(len(tour) - 1)])
            for j in range(len(tour) - 1):
                new_cost = current_cost - euclidean_distance(cities[tour[j]], cities[tour[j + 1]]) \
                                         + euclidean_distance(cities[tour[j]], cities[order[i] + 1]) \
                                         + euclidean_distance(cities[order[i] + 1], cities[tour[j + 1]])
                if new_cost < min_additional_cost:
                    min_additional_segm = (tour[j], order[i] + 1, tour[j + 1])
                    min_additional_cost = new_cost
                    min_tour = tour

        if min_tour:
            # Insert node in the best spot
            insertion_index = min_tour.index(min_additional_segm[0]) + 1
            min_tour.insert(insertion_index, order[i] + 1)

    return tours

# Procedure to calculate tour cost
def calculate_tour_cost(tours):
    tour_costs = []
    for tour in tours:
        tour.append(0)  # Return to the depot
        tour.insert(0, 0)
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        tour_costs.append(cost)
    return tour_costs, max(tour_costs)

# Generate an initial feasible solution
tours = initialize_solution()

# Calculate the distances of each tour
tour_costs, max_travel_cost = calculate_tour_cost(tours)

# Output the result
for j, tour in enumerate(tours):
    print(f"Robot {j} Tour: {tour}")
    print(f"Robot {j} Total Travel Cost: {tour_costs[j]}")
print(f"Maximum Travel Cost: {max_travel_cost}")