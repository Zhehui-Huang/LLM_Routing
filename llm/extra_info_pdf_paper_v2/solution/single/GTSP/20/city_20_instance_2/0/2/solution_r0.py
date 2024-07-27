import math

# City coordinates
coords = {
    0: (3, 26), # depot
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

# Calculate the total travel cost of a tour
def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Find the shortest tour visiting exactly one city from each group
def find_shortest_tour():
    from itertools import product
    
    min_cost = float('inf')
    best_tour = []
    
    # Generate all combinations: one city from each group
    for cities in product(groups[0], groups[1], groups[2], groups[3], groups[4]):
        # Form the tour starting and ending at the depot
        tour = [0] + list(cities) + [0]
        cost = calculate_total_travel_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Get the result
tour, total_cost = find_shortest_tour()

# Print the output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")