import math

# Define coordinates for each city, including the depot
cities = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Function to calculate Euclidean distance between any two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances between all pairs of cities
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Implement the nearest neighbor heuristic to generate an initial tour
def nearest_neighbor(start=0):
    tour = [start]
    unvisited = set(range(1, n))
    
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    tour.append(start)  # Complete the tour by returning to the depot
    return tour

# Function to assess the generated tour
def assess_tour(tour):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_distance

# Generate and assess the tour
tour = nearest_neighbor()
total_cost, max_distance = assess_tour(tour)

# Print the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))