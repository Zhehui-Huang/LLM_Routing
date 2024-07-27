import itertools
import math

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Explore all permutations of 6 cities (excluding the depot city), then add the depot city to start and end
min_cost = float('inf')
best_tour = []

for tour in itertools.permutations(cities.keys() - {0}, 6):
    current_tour = [0] + list(tour) + [0]  # start and end at depot
    current_cost = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))