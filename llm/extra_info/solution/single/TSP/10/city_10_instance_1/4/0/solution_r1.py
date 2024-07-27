from math import sqrt

# Coordinates of the cities indexed from 0 to 9
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the shortest path using the Nearest Neighbor algorithm starting from the depot
def nearest_neighbor(start):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        total_cost += distance(current_city, next_city)
        tour.append(next):city)
        current_city = next_city
        unvisited.remove(next_city)

    # Completing the tour by returning to the start city
    total_cost += distance(current_city, start)
    tour.append(start)
    return tour, total_cost

# Starting from the depot city 0
tour, total_cost = nearest_neighbor(0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")