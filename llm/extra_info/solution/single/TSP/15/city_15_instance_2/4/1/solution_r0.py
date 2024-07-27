import math

# Define the coordinates of each city, including the depot (city 0)
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Total number of cities including the depot
num_cities = len(cities)

# Implement Nearest Neighbor algorithm
def nearest_neighbor(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the depot at the end
    return tour

# Calculate the total travel cost of the tour
def calculate_total_cost(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Generate the tour starting from the depot city
tour = nearest_neighbor(0)
total_cost = calculate_total_cost(tour)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)