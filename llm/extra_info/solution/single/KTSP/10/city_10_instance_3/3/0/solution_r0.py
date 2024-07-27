import math
import itertools

# Coordinates of the cities
coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(c1, c2):
    x1, y1 = coordinates[c1]
    x2, y2 = coordinates[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours that visit exactly 7 cities and return to the depot
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    for cities in itertools.combinations(range(1, len(coordinates)), 6):
        cities = [0] + list(cities) + [0]  # Include the depot at the beginning and end
        for perm in itertools.permutations(cities[1:-1]):
            tour = [cities[0]] + list(perm) + [cities[-1]]
            distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if distance < min_distance:
                min_distance = distance
                best_tour = tour
    
    return best_tour, min_distance

# Get the shortest tour and the total travel cost
shortest_tour, total_cost = find_shortest_tour()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost}")