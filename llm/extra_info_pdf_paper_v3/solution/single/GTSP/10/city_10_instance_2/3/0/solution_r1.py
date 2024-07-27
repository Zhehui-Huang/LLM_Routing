import math
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define city coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Define city groups
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Obtain all combinations, one from each group
all_combinations = list(itertools.product(*groups))

# Find the shortest tour visiting one city from each group and returning to depot
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    
    for combination in all_combinations:
        # Start with the depot, go through each city in the combination, and return to the depot
        current_tour = [0] + list(combination) + [0]
        # Calculate the total travel cost of this tour
        current_cost = sum(euclidean_distance(cities[current_tour[i]], cities[current_tour[i+1]]) for i in range(len(current_tour) - 1))
        
        # Update the shortest found tour and its cost
        if current_cost < min_cost:
            best_tour = current_tour
            min_cost = current_cost

    return best_tour, min_cost

# Get the best tour and its cost
tour, total_cost = find_shortest_tour()

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)