import math
from itertools import product

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(groups, depot):
    # Cities with coordinates (index starting from 1 to match input format since depot is 0)
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]

    # Arrange groups with actual coordinates instead of indices
    coordinate_groups = [ [coordinates[j-1] for j in group] for group in groups]

    # Include the depot in the list of coordinates
    depot_coord = coordinates[depot-1]  
    all_possible_trips = list(product(*coordinate_groups))

    min_tour = None
    min_cost = float('inf')

    # Test all combinations of picking one city from each group
    for trip in all_possible_trips:
        # Tour goes from depot -> city from group 1 -> ... -> city from last group -> depot
        tour = [depot] + [coordinates.index(city) + 1 for city in trip] + [depot]
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(coordinates[tour[i]-1], coordinates[tour[i+1]-1])
        
        if cost < min_cost:
            min_cost = cost
            min_testinal = tour

    return min_testinal, min_cost

# Define the groups of cities indices
groups = [
    [1, 3, 5, 11, 13, 14, 19],  # Group 0
    [2, 6, 7, 8, 12, 15],       # Group 1
    [4, 9, 10, 16, 17, 18]      # Group 2
]

# The depot city index (considering 1-based index for cities in list)
depot_index = 1

# Find the shortest tour
tour, total_cost = find_shortest_tour(groups, depot_index)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")