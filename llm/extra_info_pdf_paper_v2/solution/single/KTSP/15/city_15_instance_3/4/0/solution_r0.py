import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calculate distances matrix
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to calculate the total travel distance of a tour
def calculate_tour_distance(tour):
    total_distance = 0
    for k in range(len(tour)-1):
        total_distance += distances[tour[k]][tour[k+1]]
    return total_distance

# Generate all possible tours of k cities including the depot
k = 10
all_possible_tours = permutations([i for i in cities.keys() if i != 0], k-1)

# Find the minimal tour involving the depot 0
best_tour_distance = float('inf')
best_tour = None

for tour_part in all_possible_tours:
    tour = [0] + list(tour_part) + [0]  # Starting and ending at the depot city 0
    tour_distance = calculate_tour_distance(tour)
    if tour_distance < best_tour_distance:
        best_tour_distance = tour_distance
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_distance:.2f}")