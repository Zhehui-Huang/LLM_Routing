from itertools import product
from math import sqrt

# City coordinates
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate distance between two cities
def distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate all combinations by choosing one city from each group
combinations = list(product(*groups))

# Function to find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    for combo in combinations:
        # Tour starts and ends at the depot city 0
        tour = [0] + list(combo) + [0]
        # Calculate the total distance of the tour
        total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Compare distances to find the minimum
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
    
    return best_tour, min_distance

# Get the solution
best_tour, min_distance = find_shortest_tour()

# Display the result
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))