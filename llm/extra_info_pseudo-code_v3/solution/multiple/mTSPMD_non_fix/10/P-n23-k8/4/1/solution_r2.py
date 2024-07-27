import math
from collections import defaultdict

# Helper function to calculate Euclidean distance between two cities based on their coordinates.
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the coordinates for each city, including depots.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate initial solution for robot routing.
def initial_solution(depot_indices, num_robots):
    available_cities = set(cities.keys()) - set(depot_indices)
    tours = defaultdict(list)

    # Initialize each robot's tour starting from a depot.
    for i in range(num_robots):
        tours[i].append(depot_indices[i % len(depot_indices)])

    # Assign cities to each robot's tour using nearest neighbor heuristic.
    while available_cities:
        for r in range(num_robots):
            if not available_cities:
                break
            last_city = tours[r][-1]
            nearest_city, min_distance = None, float('inf')

            for city in available_cities:
                distance = euclidean_distance(cities[last_city], cities[city])
                if distance < min_distance:
                    nearest_city, min_distance = city, distance
            
            if nearest_city is not None:
                tours[r].append(nearest_city)
                available_cities.remove(nearest_city)

    # Calculate the travel cost for each tour and print the results.
    total_cost = 0
    for r in tours:
        tour_cost = sum(euclidean_distance(cities[tours[r][i]], cities[tours[r][i + 1]]) for i in range(len(tours[r]) - 1))
        print(f"Robot {r} Tour: {tours[r]}")
        print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Enable 8 robots and assign them to 8 depots.
depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = 8

# Execute the function to solve the problem.
initial_solution(depot_indices, num_robots)