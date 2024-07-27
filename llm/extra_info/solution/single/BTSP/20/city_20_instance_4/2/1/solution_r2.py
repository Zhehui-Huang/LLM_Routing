import math

# Define the locations of the cities
city_locations = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to find the tour minimizing the maximum distance between consecutive cities
def find_tour(city_locations):
    num_cities = len(city_locations)
    visited = [False] * num_cities
    tour = [0]
    visited[0] = True
    current_city = 0
    
    while len(tour) < num_cities:
        next_city = None
        min_distance = float('inf')
        for i in range(num_cities):
            if not visited[i]:
                dist = euclidean_distance(city_locations[current_city], city_locations[i])
                if dist < min_distance:
                    min_distance = dist
                    next_city = i
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city
        
    # Closing the tour by returning to the depot
    tour.append(0)
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(city_locations[tour[i - 1]], city_locations[tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return tour, total_cost, max_distance

# Compute the tour
tour, total_cost, max_distance = find_tour(city_locations)

# Output the results 
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))