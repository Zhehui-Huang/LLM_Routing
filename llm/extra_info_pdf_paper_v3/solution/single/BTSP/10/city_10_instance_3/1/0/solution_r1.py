import math

# Define the cities as per the coordinates given
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Function to find tour using a nearest neighbor heuristic
def find_tour(start, cities, distance_matrix):
    unvisited = set(cities)
    tour = [start]
    current = start
    unvisited.remove(start)
    
    max_distance = 0

    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        max_distance = max(max_distance, distance_matrix[current][next_city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
        
    # Closing the tour by returning to the start
    tour.append(start)
    max_distance = max(max_distance, distance_matrix[current][start])

    return tour, max_distance

# Finding the tour
tour, max_distance = find_tour(0, cities, distance_matrix)

# Calculating total travel cost
total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)