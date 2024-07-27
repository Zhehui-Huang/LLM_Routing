import math
import itertools

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# City groups
city_groups = [
    [7, 9],  
    [1, 3],  
    [4, 6],  
    [8],    
    [5],    
    [2]     
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Generate all possible tours based on one city from each group, starting and ending at depot (city 0)
all_possible_tours = []
for selection in itertools.product(*city_groups):
    tour = [0] + list(selection) + [0]
    all_possible_tours.append(tour)

# Find the tour with the minimum distance
min_distance = float('inf')
best_tour = None
for tour in all_possible_tours:
    cost = total_tour_cost(tour)
    if cost < min_distance:
        min_distance = cost
        best_tour = tour

# Output the optimal tour and its cost
output = f"Tour: {best_tour}\nTotal travel cost: {min_distance:.2f}"
print(output)