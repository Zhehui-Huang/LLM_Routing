import math

# Coordinates of the 10 cities including depot city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate the Euclidean distance between two cities based on index
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Total number of cities
n = len(cities)

# Perform the nearest neighbor heuristic from the depot
# Start at the depot city 0
tour = [0]
current_city = 0
total_travel_cost = 0

# Create a set of all cities except depot (since depot is our starting point)
unvisited_cities = set(cities) - {current_city}

# Continue until all cities are visited
while unvisited_cities:
    nearest_city = None
    min_distance = float('inf')
    for city in unvisited_cities:
        distance = calculate_distance(cities[current_city], cities[city])
        if distance < min_distance:
            min_distance = distance
            nearest_city = city
    tour.append(nearest_city)
    total_travel_cost += min_distance
    current_city = nearest_city
    unvisited_cities.remove(nearest_city)

# Add the return trip back to the depot city 0
total_travel_cost += calculate_distance(cities[current_city], cities[0])
tour.append(0)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)