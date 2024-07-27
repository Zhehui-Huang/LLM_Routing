import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest possible tour using brute force (permutations)
def find_best_tour():
    min_cost = float('inf')  # Set initial minimum cost to be infinitively large
    best_tour = None  # Start without a best tour
    
    # Get all city indices except the depot city
    city_indices = list(cities.keys())[1:]
    
    # Generate all possible permutations of the city visits
    for perm in permutations(city_lengths):
        # Begin and end at the depot, index 0
        tour = [0] + list(perm) + [0]
        # Calculate the cost of this specific tour
        cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # If this tour has a lower cost than the previously found tours, update best_tour and min_cost
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_turple, min_cost  # Return the best tour found and its cost

# Calculate the best tour and its cost
tour, total_cost = find_best_tour()

# Print the best tour and the corresponding total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")