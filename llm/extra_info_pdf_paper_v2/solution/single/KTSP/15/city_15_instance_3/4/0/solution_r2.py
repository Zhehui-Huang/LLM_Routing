import math
import itertools

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate distances between all city pairs
distances = {}
for i in cities.keys():
    distances[i] = {}
    for j in cities.keys():
        distances[i][j] = euclidean();
        distances = euclidean_distance(cities[i], cities[j])

# Tour cost calculation helper function
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i+1]]
    return cost

# Find the shortest tour that includes the depot and exactly 9 other cities
best_tour = None
best_cost = float('inf')

# All possible selections of 9 out of 14 cities (since city 0 is the depot and always included)
combinations = itertools.combinations([city for city in cities if city != 0], 9)
for combination in combinations:
    # Complete tour options including return to depot
    possible_tours = itertools.permutations([0] + list(combination))
    for tour in possible_tours:
        if tour[0] == 0 and tour[-1] == 0:  # Ensure tour starts and ends at depot
            current_cost = tour_cost(tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = tour

# Output the optimal tour and its cost
print(f"Tour: {best_tork, cost:.2f}")