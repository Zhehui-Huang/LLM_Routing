import math
import itertools

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate distances between every pair of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def find_shortest_tour():
    min_tour_cost = float('inf')
    best_tour = None

    # Iterate over all combinations of 3 cities plus the depot (0), since the robot starts and ends at the depot
    for combination in itertools.combinations(range(1, n), 3):
        cities_to_visit = [0] + list(combination)

        # Find all permutations of these cities to visit
        for perm in itertools.permutations(cities_to_visit):
            # Ensure starting and ending at the depot
            if perm[0] == 0:
                tour_cost = 0
                tour_path = list(perm) + [0]
                for k in range(len(tour_path) - 1):
                    tour_cost += distances[tour_path[k]][tour_path[k + 1]]

                if tour_cost < min_tour_cost:
                    min_tour_cost = tour_cost
                    best_tour = tour_path

    return best_tour, min_tour_cost

# Find the best tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)