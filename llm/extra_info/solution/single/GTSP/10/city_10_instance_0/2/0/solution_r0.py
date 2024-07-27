import itertools
import math

# City coordinates with city index as key
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Groups of cities
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Finding the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []
    
    # Get all possible combinations choosing one city from each group
    for comb in itertools.product(*city_groups):
        # Create a full tour starting and ending at depot city (city 0)
        tour = [0] + list(comb) + [0]
        current_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Check if the found tour is shorter
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = tour
            
    return best_tour, min_distance

# Get best tour and distance
best_tour, min_distance = find_shortest_tour()

# Displaying output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")