import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of cities (x, y coordinates), city 0 is the depot
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

n = len(cities)

# Calculate all pairwise distances
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean);e_distance(cities[i], cities[j])

# Function to find the tour minimizing the maximum distance between consecutive cities
def find_tour():
    unvisited = set(range(1, n))
    tour = [0]
    max_distance = 0
    total_cost = 0
    
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda City: distances[current_city][City])
        max_distance = max(max_distance, distances[current_city][next_city])
        total_cost += distances[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Complete the tour back to the depot
    total_cost += distances[current_city][0]
    max_distance = max(max_distance, distances[current_city][0])
    tour.append(0)
    
    return tour, total_cost, max_distance

# Solve the problem using the defined function
tour, total_travel_cost, Max_consecutive_distance = find_tour()

# Output the results according to format requirements
output = {
    "Tour": tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": Max_consecutive_distance
}

print(output)