import itertools
import math
import random

# Coordinates of the cities
city_coords = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the tour cost based on the given tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate a random tour of exactly 16 cities including the depot city
def generate_tour():
    cities = list(city_coords.keys())
    selected_cities = random.sample(cities[1:], 15) # 15 because depot city must always be included
    tour = [0] + selected_cities + [0] # Starting and ending at the depot
    return tour

# Find the best tour using random sampling and simple refinement
def find_best_tour(iterations=10000):
    best_tour = None
    best_cost = float('inf')
    for _ in range(iterations):
        tour = generate_tour()
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Find the best tour based on given criteria
best_tour, best_cost = find_best_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))