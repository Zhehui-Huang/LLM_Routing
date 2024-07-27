import math
from itertools import combinations

# City coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Vehicle information
num_vehicles = 4
vehicle_capacity = 6000

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all distances
distances = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])
        distances[(j, i)] = distances[(i, j)]  # Symmetric distances

# Initialize tours
tours = [[] for _ in range(num_vehicles)]
vehicle_loads = [0] * num_vehicles

# Clarke-Wright Savings Calculation
savings = {}
for i, j in combinations(range(1, len(cities)), 2):
    s = distances[(0, i)] + distances[(0, j)] - distances[(i, j)]
    savings[(i, j)] = s

# Sorting savings in descending order
sorted_savings = sorted(savings.keys(), key=lambda x: savings[x], reverse=True)

# Assign routes based on savings while considering capacity constraints
for i, j in sorted_savings:
    if demands[i] + demands[j] > vehicle_capacity:
        continue
    assigned = False
    for k in range(num_vehicles):
        if demands[i] + demands[j] + vehicle_loads[k] <= vehicle_capacity:
            tours[k].extend([i, j])
            vehicle_loads[k] += demands[i] + demands[j]
            assigned = True
            break
    if assigned:
        break

# Two-phase and improvement would be integrated here.

# Close all tours with the depot
for k in range(num_vehicles):
    if tours[k]:
        tours[k] = [0] + tours[k] + [0]

# Calculate total distance for each tour
tour_costs = []
for k in range(num_vehicles):
    total_cost = 0
    if len(tours[k]) > 1:
        for i in range(len(tours[k]) - 1):
            total_cost += distances[tours[k][i], tours[k][i+1]]
        tour_costs.append(total_cost)
    else:
        tour_costs.append(0)

# Combine all results
overall_cost = sum(tour_costs)
results = []
for k in range(num_vehicles):
    results.append(f"Robot {k} Tour: {tours[k]}")
    results.append(f"Robot {k} Total Travel Cost: {tour_costs[k]}")
results.append(f"Overall Total Travel Cost: {overall,

for result in results:
    print(result)