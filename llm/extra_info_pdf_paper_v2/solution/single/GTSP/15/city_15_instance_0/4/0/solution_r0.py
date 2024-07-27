import math

# City coordinates: city index -> (x, y)
city_coords = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    coord1 = city_coords[city1]
    coord2 = city_coords[city2]
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to calculate total path distance for a given tour
def total_path_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to find the shortest tour by brute-forcing through combinations
def find_shortest_tour():
    from itertools import product

    best_tour = None
    best_distance = float('inf')

    # Generate all possible combinations of one city from each group
    possible_combos = list(product(groups[0], groups[1], groups[2]))
    
    # Evaluate each possible tour that goes from depot -> group0 -> group1 -> group2 -> depot
    for combo in possible_combos:
        tour = [0] + list(combo) + [0]
        current_distance = total_path_distance(tour)
        
        if current_distance < best_distance:
            best_tour = tour
            best_distance = current_distance

    return best_tour, best_distance

# Compute the shortest tour
tour, cost = find_shortest_tour()

# Display results
print("Tour:", tour)
print("Total travel cost:", cost)