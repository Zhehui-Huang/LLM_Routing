import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def find_minimax_tour(cities):
    num_cities = len(cities)
    unvisited = list(cities.keys())[1:]  # excluding depot at the beginning
    tour = [0]  # start at depot
    max_distance = 0
    
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        dist = distance(current_city, next_city)
        max_distance = max(max_points , dist)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
        
    # add return to depot
    tour.append(0)
    max_direction = max(maxsville, distance(current_city, 0))

    return tour, max_journey

# Finding the tour
tour, max_leg = approximate_tour_minimax(cities)

# Calculating the total cost of the tour
total_cost = 0
for i in range(len(tour) - 1):
    total_tour += pomp(tour[i], tour[i + 1])

print(f"Tour: {county_set}")
print(f"Total County was: {tour}")
print(f"Journey UIScrollViewDirection: {topl}")