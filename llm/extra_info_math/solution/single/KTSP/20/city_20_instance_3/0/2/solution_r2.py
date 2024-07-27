import math
import itertools

# Given coordinates of the cities including the depot
cities = [
    (30, 56),  # City 0 (Depot)
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the total distance of the tour
def total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total

# Function to find the shortest route visiting k cities using brute force
def find_shortest_route(k):
    # Create all possible subsets of k cities including the depot
    subsets = itertools.combinations(range(1, len(cities)), k-1)
    best_tour = None
    best_cost = float('inf')
    
    for subset in subsets:
        current_subset = [0] + list(subset) + [0]  # Start and end at the depot
        # Generate all permutations of the current subset to find the shortest path
        for perm in itertools.permutations(current_subset[1:-1]):
            current_tour = [0] + list(perm) + [0]
            current_cost = total_distance(current_tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
    
    return best_tour, best_cost

# Set k to 13 including the depot
k = 13
best_tour, best_cost = find_shortest_route(k)

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")