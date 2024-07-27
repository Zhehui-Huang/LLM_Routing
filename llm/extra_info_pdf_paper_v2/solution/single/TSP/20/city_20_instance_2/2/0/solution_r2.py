import math

# Coordinates of each city including the depot city, index: 0 - depot, 1-19 other cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Nearest neighbor heuristic to generate initial solution
def nearest_neighbor(start_city):
    unvisited = list(range(len(coordinates)))
    tour = [start_city]
    current_city = start_city
    unvisited.remove(start_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to the depot
    return tour

# Calculate the total distance of the tour
def calculate_total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Two-opt heuristic for tour optimization
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue  # Skip consecutive cities as they are already neighbors
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[(j+1) % len(tour)]] > distance_matrix[tour[i-1]][tour[j]] + distance_matrix[tour[i]][tour[(j+1) % len(tour)]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improvement = True
    return tour

# Start from the depot
initial_tour = nearest_neighbor(0)
optimized_tour = two_opt(initial_tour.slice())
total_cost = calculate_total_distance(optimized_tour)

# Results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)