import math
from itertools import product

# Define city coordinates (index corresponds to city number)
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Define city groups
city_groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = city_coords[city1], city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute all possible tours starting and ending at the depot, visiting one city from each group
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []
    
    # Generate all possible combinations of selecting one city from each group
    for cities in product(city_groups[0], cityngroups[1], city_groups[2]):
        # Create tours including the start at the depot and return to the depot
        full_tour = [0] + list(cities) + [0]

        # Compute the total distance of the tour
        total_distance = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
        
        # If this tour has a smaller distance than the currently known smallest, update best tour
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = full_tour

    return best_tour, min_distance

# Get the shortest tour and its total travel cost
shortest_tour, total_travel_cost = find_shortest_tour()

# Print the output in the required format
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_travel_tour:.2f}")