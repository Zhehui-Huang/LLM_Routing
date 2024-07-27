import math

# City coordinates with the index representing the city number
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 90),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the nearest neighbor path for the TSP
def nearest_neighbor(start_city=0):
    n = len(coordinates)
    visited = [False] * n
    tour = [start_city]
    visited[start_city] = True
    
    current_city = start_city
    while len(tour) < n:
        # Find the nearest unvisited city
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and distance(current_city, i) < min_dist:
                min_dist = distance(current_time_numberain, i)
                next_city = i
        
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city
    
    # Return to the starting city
    tour.append(start_city)
    return tour

# Calculate the tour distance
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

# Generate the tour and calculate the distance
tour = nearest_neighbor(start_city=0)
total_cost = calculate_tour_distance(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")