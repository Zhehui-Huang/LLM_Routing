import math
import itertools

# Coordinates of the cities including the depot
coordinates = [
    (84, 67),  # depot city 0
    (74, 40),  # city 1
    (71, 13),  # city 2
    (74, 82),  # city 3
    (97, 28),  # city 4
    (0, 31),   # city 5
    (8, 62),   # city 6
    (74, 56),  # city 7
    (85, 71),  # city 8
    (6, 76)    # city 9
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initial tour (simple nearest neighbor start)
tour = [0]
current_city = 0
remaining_cities = set(range(1, n))

while remaining_cities:
    next_city = min(remaining_cities, key=lambda x: distances[current_city][x])
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

# To complete the tour, return to depot
tour.append(0)

def calculate_total_distance(tour):
    """Calculate the total travel cost of a tour."""
    total = 0
    for i in range(1, len(tour)):
        total += distances[tour[i-1]][tour[i]]
    return total

# Calculate the total travel distance of the initial tour
total_distance = calculate_total_distance(tour)

# Simulation of Lin-Kernighan type improvements (simplified, swap mechanism)
improved = True
while improved:
    improved = False
    for i in range(1, len(tour) - 2):
        for j in range(i + 2, len(tour) - 1):
            if distances[tour[i-1]][tour[i]] + distances[tour[j]][tour[j+1]] \
                    > distances[tour[i-1]][tour[j]] + distances[tour[i]][tour[j+1]]:
                # Swap leads to shorter path, perform the swap
                tour[i:j+1] = reversed(tour[i:j+1])
                improved = True
                total_distance = calculate_total_distance(tour)

output_tour = tour
output_total_distance = total_distance

print(f"Tour: {output_tour}")
print(f"Total travel cost: {output_total_distance:.2f}")