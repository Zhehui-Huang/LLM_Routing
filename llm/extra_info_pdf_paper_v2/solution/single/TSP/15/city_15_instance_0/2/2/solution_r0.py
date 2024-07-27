import math
import random

# Coordinates of each city including the depot
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), 
    (21, 23), (88, 59), (79, 77), (63, 23), 
    (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial random tour
def initial_tour():
    tour = list(range(1, len(cities)))  # exclude the depot 0 from initial tour list
    random.shuffle(tour)
    return [0] + tour + [0]  # starting and ending at the depot

# Function to compute the total cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# 2-opt swap improvement
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # adjacent edges; no need to consider
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Generate initial tour
tour = initial_tour()
# Improve tour using 2-opt
improved_tour = two_opt(tour)
total_cost = tour_cost(improved_tour)

# Output results
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost}")