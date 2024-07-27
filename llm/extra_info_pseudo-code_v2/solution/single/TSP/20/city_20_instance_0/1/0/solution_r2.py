import math

# City coordinates (index corresponds to city number)
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial tour using a simple method such as nearest neighbor
def generate_initial_tour(start_index):
    """Generate an initial tour using the nearest neighbor heuristic."""
    n = len(cities)
    unvisited = set(range(n))
    unvisited.remove(start_index)
    tour = [start_index]
    current_city = start_index

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start_index)  # return to the start
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    """Calculate the total travel cost of a tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate tour and calculate its cost
initial_tour = generate_initial_tour(0)
tour_cost = calculate_tour_cost(initial_tour)

# Output results
print("Tour:", initial_tour)
print("Total travel cost:", tour_cost)