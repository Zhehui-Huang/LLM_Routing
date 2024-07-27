import math
import itertools

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def find_shortest_tour(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    
    # Calculate all-pair distances
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    
    # Set to store the indexes of cities to be visited, including the depot
    city_indexes = range(num_cities)
    min_cost = float('inf')
    best_tour = []

    # Check all combinations of cities to pick exactly (subset_size-1) since the depot is fixed
    for subset in itertools.combinations(city_indexes[1:], 9):
        complete_tour = [0] + list(subset) + [0]

        # Check all permutations of the selected cities beyond the depot
        for tour_perm in itertools.permutations(subset):
            tour = [0] + list(tour_perm) + [0]
            cost = total_distance(tour, distances)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

cities = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function call to get the shortest possible tour and cost
optimal_tour, optimal_cost = find_shortest_tour(cities)

# Display the tour and travel cost
print("Tour:", optimal_tour)
print("Total travel bill:", optimal_cost)