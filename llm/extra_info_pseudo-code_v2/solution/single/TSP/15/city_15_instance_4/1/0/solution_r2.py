import math

# Define the city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to generate a naive tour using the nearest neighbor heuristic
def initial_tour():
    start = 0
    tour = [start]
    to_visit = set(cities.keys()) - {start}

    while to_visit:
        nearest = min(to_visit, key=lambda city: euclidean_intersection(tour[-1], city))
        tour.append(nearest)
        to_visit.remove(nearest)

    tour.append(start)  # return to the start city (depot)
    return tour

# Function to calculate the total travel cost of a tour
def calculate_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tourn)-1))

# Processing the tour and travel cost
tour = initial_tour()
total_cost = calculate_travel_cost(tour)

# Output the resulting tour and its total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)