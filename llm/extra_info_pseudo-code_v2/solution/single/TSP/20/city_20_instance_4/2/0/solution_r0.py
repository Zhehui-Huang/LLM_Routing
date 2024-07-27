import math
from itertools import permutations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate initial tour using a simple nearest neighbor algorithm starting from depot
def initial_tour():
    remaining = set(cities.keys())
    current = 0
    tour = [current]
    remaining.remove(current)
    
    while remaining:
        next_city = min(remaining, key=lambda x: distance(current, x))
        tour.append(next_city)
        remaining.remove(next_city)
        current = next_city
    
    tour.append(0) # return to the depot
    return tour

# Calculate total travel cost of the tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Function to improve the tour using a simplistic Lin-Kernighan-like approach
def improve_tour(tour):
    min_cost = total_cost(tour)
    best_tour = tour[:]
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = total_cost(new_tour)
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
        tour = best_tour
    
    return best_tour

# Compute initial and improved tour
initial = initial_tour()
improved_tour = improve_tour(initial)

# Outputs
final_cost = total_cost(improved_tour)
print("Tour:", improved_tour)
print("Total travel cost:", final_cost)