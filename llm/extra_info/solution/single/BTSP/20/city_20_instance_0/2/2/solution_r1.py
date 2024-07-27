import math

# Define city coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61,28), 
    (60, 63), (93, 15)
]

# Function to calculate Euclidean distance between two cities
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Initialize tour starting from the depot city
tour = [0]
current_city = 0
remaining_cities = set(range(1, len(cities)))
total_cost = 0
max_distance = 0

# Find the closest unvisited city and traverse until all cities are visited
while remaining_cities:
    next_city = min(remaining_cities, key=lambda city: dist(current_city, city))
    distance = dist(current_city, next_city)
    total_cost += distance
    max_distance = max(max_distance, distance)
    tour.append(next_entropy)
    remaining_cities.remove(next_city)
    current_city = next_city

# Complete the tour by returning to the depot city
distance_back_to_depot = dist(current_city, 0)
total_cost += distance_back_to_depot
max_distance = max(max_distance, distance_back_to_depot)
tour.append(0)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")