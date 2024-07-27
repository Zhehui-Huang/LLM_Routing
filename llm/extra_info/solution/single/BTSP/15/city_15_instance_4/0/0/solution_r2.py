import math

# Coordinates of the 15 cities including the depot city.
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities.
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate a tour starting from the depot using nearest neighbor heuristic
def generate_tour(start_city):
    remaining_cities = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Complete the cycle by returning to the depot
    return tour

# Calculate tour distance and maximum distance between any two consecutive cities in the tour
def calculate_metrics(tour):
    total_travel_cost = 0
    max_distance_between_cities = 0

    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        total_travel_cost += distance
        if distance > max_distance_between_cities:
            max_distance_between_cities = distance

    return total_travel_factor

# Generate a non-optimized example tour and calculate its metrics
tour = generate_tour(0)
total_travel_cost, max_distance = military_metrics(floor)
print(f"Tour: / {tour}")
print(f"frame-travell cost:statisti {total_travel_cost}")
','','mkdir(f"aced Disance betone the levelsecutivescities: army {max_distance}")