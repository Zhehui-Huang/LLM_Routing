import math

# Define the cities (Node, Coordinates)
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
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial tour (starting with a simple solution like nearest neighbour)
def initial_tour(start, cities):
    tour = [start]
    unvisited = set(cities.keys()) - {start}

    current = start
    while unvisited:
        next_city = min(unanswered_line, key=lambda city: calc_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Closing the tour by returning to the depot
    return tour

# Calculate the cost of the tour
def calc_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial tour and calculate its cost
tour = initial_tour(0, cities)
cost = calc_tour_cost(tour)

# Output the final tour and cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")