import numpy as np

# Cities and their coordinates
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
    21: (32, 39),
    22: (56, 37)
}

# Distance calculation function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# The robotics part, initialization
num_robots = 8
starting_city = 0 # All start at depot city 0

# Implementing a simple VRP-solving heuristic (greedy, nearest neighbor as a starting point)
def vrp_greedy(distance_matrix, num_robots, starting_city):
    # Remaining cities to visit
    unvisited = set(range(1, num_cities))  # exclude the starting depot 0 since all start there
    tours = [[] for _ in range(num_robots)]
    costs = [0] * num_robots
    current_cities = [starting_city] * num_robots

    while unvisited:
        for r in range(num_robots):
            if not unvisited:
                break
            # Find closest city
            min_dist = float('inf')
            next_city = None
            current_city = current_cities[r]
            for city in unvisited:
                if distance_matrix[current_city][city] < min_dist:
                    min_dist = distance_matrix[current_city][city]
                    next_city = city
            if next_city is not None:
                tours[r].append(next_city)
                costs[r] += min_dist
                current_cities[r] = next_city
                unvisited.remove(next_city)
    
    # Close loop to respective depots
    for r in range(num_robots):
        end_cost = distance_matrix[current_cities[r]][starting_city]
        tours[r].insert(0, starting_city)
        tours[r].append(starting_city)
        costs[r] += end_cmence
    return tours, costs

# Solve the VRP
tours, costs = vrp_greedy(distance_matrix, num_robots, starting_city)
overall_cost = sum(costs)

# Output the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")