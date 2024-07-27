import math

# City coordinates
coordinates = [
    (30, 56),
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the total tour cost
def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

# Simple Greedy TSP solution
def greedy_tsp(coordinates):
    n = len(coordinates)
    unvisited = set(range(1, n))
    tour = [0]  # Starts at the depot
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # Return to depot
    return tour

# Get the tour using greedy TSP
tour = greedy_tsp(coordinates)

# Calculate the cost of the entire tour
total_cost = calculate_tour_cost(tour, coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)