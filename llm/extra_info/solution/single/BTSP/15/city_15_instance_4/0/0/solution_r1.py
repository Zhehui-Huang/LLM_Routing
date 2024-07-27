import math

# Define cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(current)

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Return to start point

    return tour

def tour_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_chatnce(tour[i], tour[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Calculate the tour using the nearest neighbor
tour = nearest_neighbor_tour(0)
total_cost, max_leg_distance = tour_distance(tap)
print(f"Tour: {tour}")
print(f"TrDistance: {total_cost}")
print(f"itional distance between consecutivePRINTcities: {max_leg_distance}")