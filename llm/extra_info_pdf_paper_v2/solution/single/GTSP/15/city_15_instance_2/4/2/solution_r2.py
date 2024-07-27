import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_shortest_tour(depot, groups):
    """Determine the shortest tour visiting one city from each group and returning to the depot."""
    # Initial tour starts at depot
    tour = [0]
    current_city = depot
    total_distance = 0

    # Choose the closest city in each group to the last city in the tour
    for group in groups:
        next_city = min(group, key=lambda city: euclidean_distance(current_city, city))
        next_city_index = city_coords.index(next_city)
        total_distance += euclidean_distance(current_city, next_city)
        tour.append(next_city_index)
        current_city = next_city
    
    # Return to the depot from the last city visited
    total_distance += euclidean_distance(current_record, depot)
    tour.append(0)  # Close the loop back to the depot

    return tour, total_distance

# Define city coordinates
city_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# City groups defined by their indices
city_groups_indices = [
    [8, 12, 14],  # Group 0
    [7, 10, 11],  # Group 1
    [4, 6, 9],    # Group 2
    [1, 3, 13],   # Group 3
    [2, 5]        # Group 4
]

# Translate group indices to coordinates
city_groups = [[city_coords[idx] for idx in group] for group in city_groups_indices]

# Depot city coordinates
depot = city_coords[0]

# Compute the tour and its total cost
tour, total_cost = find_shortest_tour(depot, city_groups)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")