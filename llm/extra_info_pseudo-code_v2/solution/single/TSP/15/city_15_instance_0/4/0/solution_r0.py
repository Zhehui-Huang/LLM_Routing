import math

# Vector of cities with coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a naive tour simply visiting cities in sequence
def naive_tour(cities):
    return list(range(len(cities)))

# Calculate the tour's total cost
def tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Simplified Lin-Kernighan algorithm-related improvement, placeholder for now
# This example does not yet incorporate it, provided as naive solution setup
def improve_tour(tour):
    # This should contain the local optimization logic
    return tour  # Returns unchanged tour for now

# Initialize the tour starting and ending at the depot
initial_tour = naive_tour(cities)
initial_tour.append(0)  # Add return to the depot

# Calculate initial tour cost
initial_cost = tour_cost(initial_tour)

# Improve the tour using a placeholder LK algorithm
improved_tour = improve_tour(initial_tour)
improved_cost = tour_cost(improved_tour)

# Output tour and cost
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {improved_cost}")