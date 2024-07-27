import math

# Cities' coordinates
cities = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), 
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist

# Approach to solve the problem using a greedy heuristic
def find_tour():
    import sys
    current_city = 0
    unvisited = set(range(1, num_cities))
    tour = [current_city]
    total_cost = 0
    max_leg_distance = 0

    while unvisited:
        next_city, next_dist = min(((city, distances[current_city][city]) for city in unvisited), key=lambda x: x[1])
        tour.append(next_city)
        total_cost += next_dist
        max_leg_distance = max(max_leg_distance, next_dist)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Close the tour
    last_leg_distance = distances[current_city][0]
    total_cost += last_leg_distance
    max_leg_distance = max(max_leg_distance, last_leg_distance)
    tour.append(0)

    return tour, total_cost, max_leg_distance

# Calculate tour, total cost, and max leg distance
tour, total_cost, max_leg_distance = find_tour()

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)