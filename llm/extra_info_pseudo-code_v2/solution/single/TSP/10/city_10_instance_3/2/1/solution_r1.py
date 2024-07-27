import math

# Define the cities with their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate an initial tour using a simple nearest neighbor heuristic
def initial_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(x, current_city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    tour.append(start_city)  # complete the loop
    return tour

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Generating the Initial Tour
initial = initial_tur(0)
initial_cost = calculate_cost(initial)

# Output the initial tour and its cost
print("Tour:", initial)
print("Total travel cost: {:.2f}".format(initial_cost))