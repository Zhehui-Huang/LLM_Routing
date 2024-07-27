import numpy as np

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
coordinates = [
    (145, 215),  # Depot city 0
    (151, 264),  # Depot city 1
    (159, 261),  # Depot city 2
    (130, 254),  # Depot city 3
    (128, 252),  # City 4
    (163, 247),  # City 5
    (146, 246),  # City 6
    (161, 242),  # City 7
    (142, 239),  # City 8
    (163, 236),  # City 9
    (148, 232),  # City 10
    (128, 231),  # City 11
    (156, 217),  # City 12
    (129, 214),  # City 13
    (146, 208),  # City 14
    (164, 208),  # City 15
    (141, 206),  # City 16
    (147, 193),  # City 17
    (164, 193),  # City 18
    (129, 189),  # City 19
    (155, 185),  # City 20
    (139, 182)   # City 21
]

# Tours provided
robot_tours = [
    [0, 0, 16, 7, 13, 3, 18, 6, 0],
    [0, 0, 19, 5, 20, 10, 14, 0],
    [0, 0, 21, 12, 11, 1, 17, 0],
    [0, 0, 4, 15, 9, 2, 8, 0]
]

# Total travel cost calculation
computed_costs = [259.37, 231.88, 215.09, 178.71]
computed_total_cost = 885.05

# Check if tours visit all cities exactly once
visited_cities = set()
for tour in robot_tours:
    visited_cities.update(tour)

# Check if all cities are visited exactly once
all_cities_visited = (len(visited_cities) == 22)

# Check if tours start and finish at coded depots
tours_correct_start_end = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours)

# Calculate travel cost for each tour and total
calculated_costs = []
for tour in robot_tours:
    tour_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    calculated_costs.append(tour_cost)

calculated_total_cost = sum(calculated_costs)

# Check within a margin of error due to floating point arithmetic
costs_match = all(np.isclose(computed, calculated, rtol=0.01) for computed, calculated in zip(computed_costs, calculated_costs))
total_cost_match = np.isclose(computed_total_cost, calculated_total_cost, rtol=0.01)

# Final check
if all_cities_visited and tours_correct_start_end and costs_match and total_cost_match:
    print("CORRECT")
else:
    print("FAIL")