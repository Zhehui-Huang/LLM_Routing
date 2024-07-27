import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Groups of cities
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Calculate Euclidean distance between two cities
def euclidean_dist(id1, id2):
    return math.sqrt((cities[id1][0] - cities[id2][0]) ** 2 + (cities[id1][1] - cities[id2][1]) ** 2)

# Calculate distance for a given tour
def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_dist(tour[i], tour[i + 1])
    return total_dist

# Find the shortest tour that visits one city from each group and returns to the depot
def find_shortest_tour():
    from itertools import product

    best_tour = None
    best_distance = float('inf')

    # Generate all combinations of choices where you pick one city from each group
    for combination in product(*groups):
        current_tour = [0] + list(combination) + [0]  # Start and end at the depot
        current_distance = calculate_total_distance(current_tour)
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = current_tour

    return best_tour, best_distance

# Execute the function to find the solution
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)