import math
import itertools

# Define city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances between cities
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic initial tour using Nearest Neighbor approach
def nearest_neighbor_tour(start=0):
    unvisited = set(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start)  # return to the depot
    return tour

# Calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Initial tour
initial_tour = nearest_neighbor_tour()
initial_cost = calculate_tour_cost(initial_tour)

# Print initial solution
print("Initial tour: ", initial_tour)
print("Initial total travel cost: ", initial_cost)

# Placeholder for a more sophisticated Lin-Kernighan Improvement - Simplified here
# In real scenario this would be a complex function to build, involving many edge swaps and local search strategies
def improve_tour_with_lin_kernighan(tour):
    # This is a placeholder showing where we'd implement such logic
    return tour, calculate_tour_cost(tour)

# Attempt to improve the tour (dummy improvement function here)
improved_tour, improved_cost = improve_tour_with_lin_kernighan(initial_tour)

print("Improved Tour: ", improved_tour)
print("Total travel cost: ", improved_cost)