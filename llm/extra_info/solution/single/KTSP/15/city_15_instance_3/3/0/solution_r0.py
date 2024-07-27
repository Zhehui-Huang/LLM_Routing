import math
import itertools

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def find_shortest_tour(cities):
    num_cities = len(cities)
    distances = [[0]*num_cities for _ in range(num_cities)]
    
    # Calculate distances between all pairs of cities
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = distance(cities[i], cities[j])
    
    # Minimum distance initialization
    min_tour_cost = float('inf')
    min_tour = []
    
    # Iterate through combinations of selecting 9 cities since city 0 is fixed
    for combination in itertools.combinations(range(1, num_cities), 9):
        current_cities = [0] + list(combination)
        
        # Permutations for finding the shortest route among the selected cities
        for perm in itertools.permutations(current_cities[1:]):
            tour = [0] + list(perm) + [0]
            cost = total_distance(tour, distances)
            if cost < min_tour_cost:
                min_tour_cost = cost
                min_tour = tour
    
    return min_tour, min_tour_cost

# Define city coordinates (ID corresponds to index)
cities = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),  # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79),  # City 14
]

# Finding the required tour
optimal_tour, optimal_cost = find_shortest_tour(cities)

# Output
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)