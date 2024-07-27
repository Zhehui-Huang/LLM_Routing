import math

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate Euclidean distance
def calc_distance(i1, i2):
    x1, y1 = cities[i1]
    x2, y2 = cities[i2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Simple nearest neighbor heuristic for initial tour
def nearest_neighbor(start=0):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Calculate total cost of the tour
def total_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initialize the tour with nearest neighbor heuristic
initial_tour = nearest_neighbor(0)

# Calculate the total travel cost
travel_cost = total_tour_cost(initial_tour)

# Prepare and print the output
print("Tour:", initial_tour)
print("Total travel cost:", travel_cost)