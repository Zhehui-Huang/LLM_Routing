import math

# Define the coordinates of each city including the depot
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize tour starting from the depot
tour = [0]
remaining_cities = set(cities.keys()) - {0}

# Function to find next city minimizing the maximum edge cost
def find_next_city(current_city):
    next_city = None
    min_max_distance = float('inf')
    for city in remaining_cities:
        dist = distance(current_city, city)
        if dist < min_max_distance:
            min_max_distance = dist
            next_city = city
    return next_city

# Construct the tour
while remaining_cities:
    next_city = find_next_city(tour[-1])
    tour.append(next_city)
    remaining_cities.remove(next_city)

# Returning to the depot
tour.append(0)

# Calculate the total travel cost and the maximum distance between any two consecutive cities
total_travel_cost = 0
maximum_consecutive_distance = 0
for i in range(len(tour) - 1):
    dist = distance(tour[i], tour[i+1])
    total_travel_cost += dist
    maximum_consecutive_distance = max(maximum_consecutive_distance, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {maximum_consecutive_distance}")