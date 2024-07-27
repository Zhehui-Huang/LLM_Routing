import math
import random

# Define the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize a random tour
def create_initial_tour(city_count):
    tour = list(range(city_count))
    random.shuffle(tour)
    tour.append(tour[0])  # returning to the start point
    return tour

# Calculate tour length
def tour_length(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# 2-opt Swap which is a base part for the LK heuristic
def two_opt(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

# Basic Lin-Kernighan algorithm starting point
def lin_kernighan(tour):
    improvement = True
    best_tour = tour
    while improvement:
        improvement = False
        best_distance = tour_length(best_tour)
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt(best_tour, i, k)
                new_distance = tour_length(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improvement = True
                    break
            if improvement:
                break
    
    return best_tour

# Finding an optimal tour using the Lin-Kernighan algorithm
city_count = len(cities)
initial_tour = create_initial_tour(city_count)
lk_tour = lin_kernighan(initial_tour)
total_distance = tour_length(lk_tour)

# Output results
print("Tour:", lk_tour)
print(f"Total travel cost: {total_distance:.2f}")