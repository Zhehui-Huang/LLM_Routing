import random
import math

# City coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Groups of cities
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate an initial random tour
def initial_tour():
    tour = [0]  # start at the depot
    selected = set()
    for group in groups:
        city = random.choice(group)
        tour.append(city)
        selected.add(city)
    tour.append(0)  # return to the depot
    return tour

# Calculate the cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial tour and calculate its cost
initial = initial_tour()
init_cost = tour_cost(initial)

print(f"Initial tour: {initial}")
print(f"Initial tour cost: {init_cost}")