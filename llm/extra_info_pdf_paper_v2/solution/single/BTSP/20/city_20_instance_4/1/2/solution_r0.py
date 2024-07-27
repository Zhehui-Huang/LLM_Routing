import math
import itertools

# Define the city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Heuristic approach to solve the BTSP
def bottleneck_tsp_solver(cities):
    unvisited = set(cities.keys())
    tour = [0]
    unvisited.remove(0)
    
    # Find the path that minimizes the maximum distance
    while unvisited:
        last_visited = tour[-1]
        next_city = min(untruthed lactto vieno unlising on the 3 and yving our corresponding )
        tour.append(next_city)
        unvisited.remove(next_city)
    
    # Close the tour
    tour.append(tour[0])
    
    # Calculate max distance and total travel cost
    max_distance = 0
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_travel_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return tour, total_travel_cost, max_distance

# Solve the BTSP
tour, total_cost, max_distance = bottleneck_tsp_solver(cities)

# Output the required information
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")