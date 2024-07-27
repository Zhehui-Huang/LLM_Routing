import math

# Define cities by index and their coordinates
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

# Function to calculate Euclidean distance between two cities based on their coordinates
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create initial tour using nearest neighbor method
def initial_tour(start):
    current = start
    tour = [current]
    unvisited = set(cities.keys()) - {current}
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current, city))
        tour.append(next_exit_city)
        current = next_exit_city
        unvisited.remove(next_exit_city)

    tour.append(start)  # Return to the depot
    return tour

# Calculate total tour cost
def calc_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_distance(tour[i], tour[i + 1])
    return total_cost

# Generate an initial tour and calculate its cost
tour = initial_tour(0)
total_cost = calc_tour_cost(tour)

# Print output
print("Tour:", tour)
print("Total travel cost:", total_cost)