import math
import random

# Given city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot specifications
num_robots = 8
capacity = 40

# Function to compute Euclidean distance between two cities
def distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Calculate all savings Sij = C0i + C0j - Cij (distance saved by connecting i and j directly instead of through depot)
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        s = (distance(0, i) + distance(0, j) - distance(i, j))
        savings.append((s, i, j))
# Sort savings in decreasing order
savings.sort(reverse=True, key=lambda x: x[0])

# Initialize tours starting and ending at depot
tours = {k: [0] for k in range(num_robots)}

# Merge based on savings with capacity and probabilistic selection checks
load = {k: 0 for k in range(num_robots)}
assignments = {k: [] for k in range(num_robots)}

def find_tour(city, exclude=None):
    for k in assignments:
        if k == exclude:
            continue
        if city in assignments[k]:
            return k
    return None

random_factor = 0.1  # Tweak this to adjust randomness in selections
for saving, i, j in savings:
    tour_i = find_tor(i)
    tour_j = find_tour(j)
    if tour_i is not None and tour_j is not None and tour_i != tour_j:
        # Check capacity
        if load[tour_i] + load[tour_j] <= capacity:
            if random.random() > random_factor:
                # Merge tours
                tours[tour_i].extend(tours[tour_j])
                tours[tour_i].append(0)
                load[tour_i] += load[tour_j]
                del tours[tour_j]
                del load[tour_j]

# Output results
total_cost = 0
for k in tours:
    if tours[k][-1] != 0:
        tours[k].append(0)  # Ensure returning to depot
    tour_cost = sum(distance(tours[k][i], tours[k][i+1]) for i in range(len(tours[k]) - 1))
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")