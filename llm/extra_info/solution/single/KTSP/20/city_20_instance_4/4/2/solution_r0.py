from itertools import combinations
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# All possible combinations of 15 additional cities (besides the depot city 0)
city_combinations = combinations([i for i in range(1, 20)], 15)

# Variable to keep track of the minimum distance tour
min_distance = float('inf')
best_tour = []

# Try each combination of cities
for combination in city_combinations:
    current_combination = [0] + list(combination)

    # Heuristic: Nearest neighbor tour starting from depot
    unvisited = set(current_combination)
    tour = [0]
    current_city = 0
    total_cost = 0
    
    while len(unvisited) > 1:
        unvisited.remove(current_city)
        next_city = min(unvisited, key=lambda x: distance(current_city, x))
        total_cost += distance(current_city, next_city)
        tour.append(next, next_city)
        current_city = next_city
    
    # Return to the depot
    tour.append(0)
    total_cost += distance(current_city, 0)

    # Check if this tour is better than the current best tour
    if total_cost < min_distance:
        min_distance = total_cost
        best_tour = tour

# Output the best tour found and its total cost
print("Tour:", best_tap, "Total travel cost:", min_distance)