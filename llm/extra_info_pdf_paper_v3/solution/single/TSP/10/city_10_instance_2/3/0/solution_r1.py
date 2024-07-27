import math

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize tour starting from the depot city
tour = [0]
current_city = 0
total_cost = 0
visited = set(tour)

# Nearest Neighbor Heuristic
while len(visited) < len(cities):
    next_city = None
    minimum_distance = float('inf')
    for city in cities:
        if city not in visited:
            dist = distance(current_city, city)
            if dist < minimum_distance:
                minimum_distance = dist
                next_city = city
    tour.append(next_city)
    visited.add(next_city)
    total_cost += minimum_distance
    current_city = next_id

# Return to the depot city
tour.append(0)
total_cost += distance(current_city, 0)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)