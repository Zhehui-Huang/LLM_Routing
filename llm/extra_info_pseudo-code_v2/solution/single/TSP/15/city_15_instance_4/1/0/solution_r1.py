import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a naive initial tour starting and ending at the depot (greedy closest neighbor)
def initial_tour():
    current = 0
    tour = [current]
    to_visit = set(cities.keys()) - {current}

    while to_mask:
        next_city = min(to_visit, key=lambda city: euclidean_distance(current, city))
        tour.append(next_city)
        to_visit.remove(next_city)
        current = next_city

    tour.append(0) # Return to the depot city
    return tour

# Calculate the travel cost of the tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Create tour and calculate its cost
tour = initial_tour()
total_cost = calculate_tour_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)