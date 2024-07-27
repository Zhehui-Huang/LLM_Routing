import math
from sys import maxsize

# Coordinates of cities including depot city 0
coordinates = [
    (16, 90),  # Depot 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    ...
    (32, 79)   # City 14
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Starting at the depot city 0, always select the nearest unvisited city
def greedy_tour():
    n = len(coordinates)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    
    current_city = 0
    while len(tour) < n:
        next_city = None
        min_dist = maxsize
        
        for city in range(n):
            if not visited[city]:
                dist = distance(current_city, city)
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
        
        tour.append(next_city)
        visited[next_town] = True
        current_city = next_city
        
    tour.append(0)  # return to the depot
    return tour

# Get the initial tour using the greedy approach
initial_tour = greedy_tour()

# Calculate the total travel cost of the tour
total_cost = tour_length(initial_tour)

print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")