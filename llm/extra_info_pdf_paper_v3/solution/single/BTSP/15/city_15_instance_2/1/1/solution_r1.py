import math

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_tour(cities):
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    tour.append(0)
    return tour

# Find the tour
tour = find_tour(cities)

# Calculate the tour cost and maximum distance between any two consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = distance(tour[i], tour[i+1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Printing the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))