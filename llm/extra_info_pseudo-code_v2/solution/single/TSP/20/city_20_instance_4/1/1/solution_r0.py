import math
from heapq import heappush, heappop

# Cities coordinates where each tuple is (x, y)
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# Nearest neighbour algorithm to get a basic initial tour
def nearest_neighbour_tour(start):
    tour = [start]
    unvisited = set(cities.keys())
    unvisited.remove(start)
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # Returning to the depot
    return tour

# Calculating the cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Initial solution based on Nearest Neighbour
initial_tour = nearest_neighbour_tour(0)
initial_cost = calculate_tour_cost(initial_tour)

# Placeholder for using Lin-Kernighan Algorithm which is complex to implement fully here
# For now, we return the initial solution and its cost
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost}")