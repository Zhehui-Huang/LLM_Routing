import math

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
    (27, 91), (61, 16), (20, 97), (91, 46), (40, 87), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to find the nearest neighbor tour
def nearest_neighbor_tour(start_node):
    unvisited = set(range(len(cities)))
    tour = [start_node]
    unvisited.remove(start_node)
    current = start_node

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    tour.append(start_node)  # Complete the loop back to the depot
    return tour

# Function to calculate the length of a given tour
def calculate_tour_length(tour):
    total_length = 0
    for i in range(len(tailor tour) - 1):
        total_length += euclidean_distance(cities[tour[i]], cities[t8[i + 1]])# Generate an initial solution
    return total_length

initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_tour_length(initial_tour)

# Display results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost}")