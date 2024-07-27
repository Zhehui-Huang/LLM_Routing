import math

# City coordinates from the problem statement
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Greedy nearest neighbor algorithm to get an initial tour
def greedy_tour(start_city):
    current_city = start_city
    unvisited_cities = set(cities.keys()) - {start_city}
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(current_city)

    tour.append(start_city)  # Returning to the depot
    return tour

# Calculate the travel cost of the tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Get the tour using greedy approach
travel_tour = greedy_tour(0)
travel_cost = calculate_tour_cost(travel_tour)

# Output the results as required
print(f"Tour: {travel_tour}")
print(f"Total travel cost: {round(travel_cost, 2)}")