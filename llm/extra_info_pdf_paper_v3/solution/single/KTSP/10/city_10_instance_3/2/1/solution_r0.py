import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def all_possible_subsets(n, k, start):
    for subset in itertools.combinations(range(1, n), k-1):
        yield [start] + list(subset)

def find_best_tour(cities, k):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    best_tour = None
    best_cost = float('inf')
    
    # Generate all possible subsets of k cities including the depot (city 0)
    for subset in all_possible_subsets(n, k, 0):
        # Generate all possible permutations of the chosen subset to find the best tour
        for permutation in itertools.permutations(subset):
            if permutation[0] == 0:  # Ensure tour starts/ends at the depot
                tour = list(permutation) + [0]  # returning to the depot
                cost = calculate_total_cost(tour, distances)
                if cost < best_cost:
                    best_cost = cost
                    best_tour = tour
    
    return best_tour, best_cost

# Define the cities coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# We need to visit exactly 7 cities, including the depot
k = 7
best_tour, best_cost = find_best_tour(cities, k)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")