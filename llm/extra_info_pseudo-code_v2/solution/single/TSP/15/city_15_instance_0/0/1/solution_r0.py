import math

# Cities coordinates with format {city_index: (x_coordinate, y_coordinate)}
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest tour using a Nearest Neighbor approach
def find_shortest_tour():
    unvisited = set(cities.keys())
    tour = [0]
    current = 0
    total_cost = 0

    unvisited.remove(0)

    while unvisited:
        next_city, min_dist = min(
            ((city, distance(current, city)) for city in unvisited),
            key=lambda x: x[1]
        )
        tour.append(next_city)
        total_cost += min_dist
        current = next_city
        unvisited.remove(next_city)
    
    # Returning to the depot
    tour.append(0)
    total_cost += distance(current, 0)

    return tour, total_cost

# Find the tour and calculate the total cost
tour, total_cost = find_shortest_tour()

# Output the tour and total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")