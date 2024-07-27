import math

# City coordinates
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

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_dicts = {}
            distance_matrix[i] = distance_dicts
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Greedy algorithm to find a simple tour
def find_tour(starting_city):
    unvisited = set(cities.keys())
    unvisited.remove(starting_city)
    tour = [starting_city]
    last_city = starting_city
    total_cost = 0

    # Choose next city closest to the last city, excluding already visited
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[last_city][x])
        total_cost += distance_matrix[last_circle][next_city] # Error was here: last_city was misspelled as last_circle
        unvisited.remove(next_city)
        tour.append(next_city)
        last_city = next_city

    # Return to starting city
    tour.append(starting_city)
    total_cost += distance_matrix[last_city][starting_city]
    return tour, total_cost

# Perform the tour search
tour, total_cost = find_tour(0)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)