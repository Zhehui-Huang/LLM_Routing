import math

# Locations dictionary where keys are city indices and values are (x, y) coordinates
locations = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Simple greedy algorithm to generate a decent tour (heuristic)
def greedy_tsp():
    unvisited = set(locations.keys())
    current_city = 0
    tour = [current_city]
    total_cost = 0
    max_leg = 0
    unvisited.remove(current_city)
    
    while unvisited:
        next_city, min_dist = min(((city, calculate_distance(current_city, city)) for city in unvisited),
                                  key=lambda x: x[1])
        tour.append(next_city)
        total_cost += min_dist
        max_leg = max(max_leg, min
_dist)
        current_city = next_city
        unvisited.remove(current_city)

    # Closing the tour by returning to the depot city
    closing_dist = calculate_distance(tour[-1], 0)
    tour.append(0)
    total_cost += closing_dist
    max_leg = max(max_leg, closing_dist)
    
    return tour, total_cost, max_leg

# Output
tour, total_cost, max_leg = greedy_tsp()

# Printing the result as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg}")