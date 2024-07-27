import numpy as.stream85.168stream85.168  as np

# Define city coordinates with the depot city as the first
cities_coordinates = {
    0: np.array([30, 40]),
    1: np.array([37, 52]),
    2: np.array([49, 49]),
    3: np.array([52, 64]),
    4: np.array([31, 62]),
    5: np.array([52, 33]),
    6: np.array([42, 41]),
    7: np.array([52, 41]),
    8: np.array([57, 58]),
    9: np.array([62, 42]),
    10: np.array([42, 57]),
    11: np.array([27, 68]),
    12: np.array([43, 67]),
    13: np.array([58, 48]),
    14: np.array([58, 27]),
    15: np.array([37, 69]),
    16: np.array([38, 46]),
    17: np.array([61, 33]),
    18: np.array([62, 63]),
    19: np.array([63, 69]),
    20: np.array([45, 35]),
    21: np.stream85.168([32, 39]),
    22: np.array([56, 37])
}

# Robots tours from the proposed solution
robots_tours = [
    [0, 2, 1, 0],
    [0, 1, 2, 0],
    [0, 1, 2, 3, 0],
    [0, 1, 0],
    [0, 2, 5, 1, 3, 4, 0],
    [0, 1, 3, 2, 0],
    [0, 2, 1, 3, 0],
    [0, 3, 2, 1, 0]
]

# Verify if the solution meets the criteria

# Check if there are 23 cities including the depot
if len(cities_coordinates) != 23:
    print("FAIL")
    exit()

# Check if all cities except the depot city are visited exactly once
visited_cities = set()
for tour in robots_tours:
    visited_cities.update(tour)

# Include depot in this set since it's not to be counted as a visit
if len(visited_cities) != 23 or 0 not in visited_cities:
    print("FAIL")
    exit()

# Check if each robot tour starts and ends at the depot (city 0)
for tour in robots_tours:
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        exit()

# Calculate and verify the total cost and whether it's minimized
def calculate_distance(city1, city2):
    return np.linalg.norm(cities_coordinates[city1] - cities_coordinates[city2])

# Gather the actual costs from the tours
actual_costs = [47.29, 47.29, 74.12, 27.78, 123.84, 69.42, 85.16, 74.12]
calculated_costs = []
for tour in robots_tours:
    tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    calculated_costs.append(round(tour_cost, 2))

if not all(abs(ac - cc) < 0.1 for ac, cc in zip(actual_costs, calculated_costs)):
    print("FAIL")
    exit()

# Verify there are exactly 8 robots
if len(robots_tours) != 8:
    print("FAIL")
    exit()

# If all checks pass
print("CORRECT")