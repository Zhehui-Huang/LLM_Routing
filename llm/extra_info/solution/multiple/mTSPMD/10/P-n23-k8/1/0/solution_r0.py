import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the coordinates of each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Assign depots to each robot
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = len(depots)

# Optimize each robot's tour independently (for the sake of this example, let's use a simple greedy algorithm)
def greedy_tour(start_city):
    remaining = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    while remaining:
        next_city = min(remaining, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        remaining.remove(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

# Generate the tours for each robot
tours = [greedy_tour(depot) for depot in depots]

# Calculate the cost of each tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

tour_costs = [calculate_tour_cost(tour) for tour in tours]

# Display the results
overall_cost = sum(tour_costs)
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")