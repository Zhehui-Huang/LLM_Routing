import math
import itertools

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
    return total_time

# Generate all possible tours of k=10 cities including the depot
best_tour = None
best_distance = float('inf')

# Selecting combinations of 9 additional cities since depot city 0 must be included
for cities_combo in itertools.combinations([i for i in cities if i != 0], 9):
    current_cities = [0] + list(cities_combo)  # Include depot city
    for tour in itertools.permutations(current_cities):
        # Ensure tour begins and ends at the depot city 0
        if tour[0] == 0 and tour[-1] == 0:
            distance = calculate_tour_distance(tour)
            if distance < best_distance:
                best_distance = distance
                best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")