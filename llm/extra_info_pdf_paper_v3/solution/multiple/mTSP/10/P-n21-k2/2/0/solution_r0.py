import numpy as np
import itertools

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between each pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
    return distances

distances = calculate_distances(cities)

### Step 2: Initial Solution Using a Heuristic
# Nearest neighbor heuristic to create an initial solution
def nearest_neighbor_tour(starting_city, cities, distances):
    tour = [starting_city]
    unvisited = set(cities) - {starting_city}

    current_city = starting_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(starting_city)  # returning to the depot
    return tour

# Generating initial solutions for each robot
robot_tours = [
    nearest_neighbor_tour(0, range(1, 11), distances),  # First half of the cities for robot 0
    nearest_neighbor_tour(0, range(11, 21), distances)  # Second half of the cities for robot 1
]

### Step 3: 2-Opt Improvement
def two_opt(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distances[tour[i]][tour[i-1]] + distances[tour[j+1]][tour[j]] > \
                   distances[tour[i]][tour[j]] + distances[tour[i-1]][tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Optimizing each robot's tour using 2-opt
optimized_robot_tours = [two_opt(tour, distances) for tour in robot_tours]

### Step 4: Calculate the travel cost for each tour
def tour_cost(tour, distances):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i + 1]]
    return cost

robot_costs = [tour_cost(tour, distances) for tour in optimized_robot_tours]
overall_cost = sum(robot_costs)

### Output Results
for idx, (tour, cost) in enumerate(zip(optimized_robot_tours, robot_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")