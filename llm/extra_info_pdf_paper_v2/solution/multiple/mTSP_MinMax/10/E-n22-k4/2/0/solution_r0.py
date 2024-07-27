import math
from collections import defaultdict

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates (indexed from 0)
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

robot_count = 4
depot = 0

# Initialize tours (simple round robin assignment excluding depot)
tours = defaultdict(list)
for i, city in enumerate(cities[1:], start=1):
    tours[i % robot_count].append(city)

# Convert tours to indices for output purposes
tour_indices = {i: [0] + [cities.index(city) for city in tours[i]] + [0] for i in tours}

# Calculate travel cost for each tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        a, b = tour[i], tour[i + 1]
        cost += euclidean_distance(cities[a], cities[b])
    return cost

tour_costs = {i: calculate_tour_cost(tour_indices[i]) for i in tour_indices}

# Calculate the maximum travel cost
max_cost = max(tour_costs.values())

# Output
for i in tour_indices:
    print(f"Robot {i} Tour: {tour_indices[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")
print(f"Maximum Travel Cost: {max_cost}")