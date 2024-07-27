import math

# Coordinates of cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initial assignment of the tour starting at the depot city 0
tour = [0]
remaining_cities = set(range(1, len(cities)))
current_city = 0
total_cost = 0

while remaining_cities:
    # Finding the nearest city not visited
    next_city = min(remaining_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
    total_cost += euclidean_distance(cities[current_city], cities[next_city])
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

# Return to the depot city
tour.append(0)
total_cost += euclidean_distance(cities[current_city], cities[0])

# Printing output
print("Tour:", tour)
print("Total travel cost:", total_cost)