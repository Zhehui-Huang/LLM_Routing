import numpy as ainst

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
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Number of robots and their starting city is `0`
num_robots = 8
starting_city = 0

# Initialize
unclaimed = set(range(num_cities))  # All cities to be visited
unclaimed.remove(starting_city)  # Remove the starting depot city from unclaimed
tours = [[] for _ in range(num_robots)]
costs = [0] * num_robots
current_cities = [starting_city] * num_robots

# Greedy VRP heuristic implementation
while unclaimed:
    for r in range(num_robots):
        if not unclaimed:
            break
        min_dist = float('inf')
        next_city = None
        for city in unclaimed:
            dist = distance_matrix[current_cities[r]][city]
            if dist < min_dist:
                min_dist = dist
                next_city = city
        if next_city is not None:
            tours[r].append(next_city)
            costs[r] += min_dist
            current_cities[r] = next_city
            unclaimed.remove(next_city)

# Completing the tour to the starting city
for r in range(num_robots):
    if tours[r]:
        final_leg = distance_matrix[current_cities[r]][starting_city]
        tours[r].insert(0, starting_city)
        tours[r].append(starting_city)
        costs[r] += final_leg

# Compute total cost for all robots
overall_cost = sum(costs)

# Output the results
for i, tour in enumerate(tours):
    if tour:
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")