import math
from itertools import permutations

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create an initial tour using nearest neighbor heuristic
def nearest_neighbor_tour(start):
    unvisited = set(range(1,len(coordinates)))
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start)  # return to the depot
    return tour

# 2-opt Swap function
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # skip consecutive nodes
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Calculate the cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial tour and improve it with 2-opt
initial_tour = nearest_neighbor_tour(0)
improved_tour = two_opt(initial_tour)
total_cost = tour_cost(improved_tour)

# Output the tour and total cost
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost}")