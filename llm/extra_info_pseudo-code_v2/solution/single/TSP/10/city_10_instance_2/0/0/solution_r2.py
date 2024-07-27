import math

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to determine the initial tour using a nearest neighbor approach
def initial_tour(start_city):
    tour = [start_city]
    unvisited = set(cities.keys()) - {start_city}
    current = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start_city)  # return to start city
    return tour

# Calculate the total cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_distance(tour[i], tour[i+1])
    return total_cost

# Calculate initial tour and its cost
initial_tour = initial_tour(0)
tour_cost = calculate_tour_cost(initial_tour)

# Output the initial tour and its cost
print("Tour:", initial_tour)
print("Total travel cost:", tour_cost)