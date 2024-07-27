import math
from itertools import product

# Define the cities and groups
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance
def euclidean_dist(city1_id, city2_id):
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest tour that visits exactly one city from each group
def find_shortest_tour(cities, groups):
    min_distance = float('inf')
    best_tour = []
    
    # Generate all combinations of cities by taking one city from each group
    for combination in product(*groups):
        # Possible tours start and end at the depot
        possible_tour = [0] + list(combination) + [0]
        current_distance = 0
        
        # Calculate the distance of this possible tour
        for i in range(len(possible_tour) - 1):
            current_distance += euclidean_dist(possible_tour[i], possible_tour[i + 1])
        
        # Update the best tour if current is shorter
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = possible_tour
            
    return best_tour, min_distance

# Main execution to find the tour and its cost
final_tour, total_cost = find_shortest_tour(cities, groups)
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")