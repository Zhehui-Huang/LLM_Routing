import math
import itertools

# City coordinates
cities = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Helper function to calculate Euclidean distance
def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest tour considering one city from each group
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate all permutations representing selecting one city from each group
    for selection in itertools.product(*city_groups):
        # Create a tour starting and ending at the depot (city 0)
        tour = [0] + list(selection) + [0]
        # Calculate the total travel cost
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        
        # Update minimum cost and best tour if a new minimum is found
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Calculating the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output optimal tour and cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")