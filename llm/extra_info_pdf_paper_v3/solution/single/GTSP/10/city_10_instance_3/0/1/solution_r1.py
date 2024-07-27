import math

# Define the coordinates of each city including the depot city
coordinates = [
    (84, 67),  # Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Define the groups
city_groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest tour visiting one city from each group
def find_shortest_tour(depot, groups):
    import itertools
    min_path = None
    min_cost = float('inf')

    # Generate all combinations for visiting one city from each group
    for combination in itertools.product(*groups):
        path = [depot] + list(combination) + [depot]
        total_cost = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            min_path = path

    return min_path, min_cost

# Compute the shortest tour and total cost
shortest_tour, total_travel_cost = find_shortest_tour(0, city_groups)

# Output the solution
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")