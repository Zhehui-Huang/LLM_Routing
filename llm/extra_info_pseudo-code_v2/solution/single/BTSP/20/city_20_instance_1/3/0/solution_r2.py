import math

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Euclidean distance calculation function
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Nearest neighbor heuristic to generate an initial tour
def nearest_neighbor_tour(start=0):
    unvisited = set(range(1, len(cities)))  # Exclude the depot initially
    tour = [start]  # Start at the depot
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Return to the depot
    return tour

# Get the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour()

# Function to calculate total and max distance of the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = calc_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
            
    return total_cost, max_distance

# Evaluate the tour
total_cost, max_distance = evaluate_tour(tour)

# Print result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")